import struct, os

def compile_po(po_path, mo_path):
    translations = {}
    msgid = None
    msgstr = None
    in_msgid = False
    in_msgstr = False

    with open(po_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if line.startswith('msgid '):
                if msgid is not None and msgstr:
                    translations[msgid] = msgstr
                raw = line[6:].strip()
                if raw.startswith('"') and raw.endswith('"'):
                    msgid = raw[1:-1]
                in_msgid = True
                in_msgstr = False
                msgstr = None
            elif line.startswith('msgstr '):
                raw = line[7:].strip()
                if raw.startswith('"') and raw.endswith('"'):
                    msgstr = raw[1:-1]
                in_msgid = False
                in_msgstr = True
            elif line.startswith('"') and line.endswith('"'):
                val = line[1:-1]
                if in_msgid and msgid is not None:
                    msgid += val
                elif in_msgstr and msgstr is not None:
                    msgstr += val
            else:
                in_msgid = False
                in_msgstr = False

        if msgid is not None and msgstr:
            translations[msgid] = msgstr

    # Add required charset header
    translations[''] = (
        'Content-Type: text/plain; charset=UTF-8\n'
        'Content-Transfer-Encoding: 8bit\n'
    )
    translations = {k: v for k, v in translations.items() if v}

    keys = sorted(translations.keys())
    n = len(keys)

    MAGIC = 0x950412de
    offsets = []
    ids_data = b''
    strs_data = b''

    for k in keys:
        v = translations[k]
        kb = k.encode('utf-8')
        vb = v.encode('utf-8')
        offsets.append((len(kb), len(ids_data), len(vb), len(strs_data)))
        ids_data += kb + b'\x00'
        strs_data += vb + b'\x00'

    header_size = 28
    ids_table_offset = header_size
    strs_table_offset = ids_table_offset + n * 8
    ids_offset = strs_table_offset + n * 8
    strs_offset = ids_offset + len(ids_data)

    output = struct.pack('<IIIIIII',
        MAGIC, 0, n,
        ids_table_offset, strs_table_offset,
        0, 0
    )

    for length, offset, _, _ in offsets:
        output += struct.pack('<II', length, ids_offset + offset)
    for _, _, length, offset in offsets:
        output += struct.pack('<II', length, strs_offset + offset)

    output += ids_data + strs_data

    os.makedirs(os.path.dirname(mo_path), exist_ok=True)
    with open(mo_path, 'wb') as f:
        f.write(output)
    print(f'Compiled {n} translations -> {mo_path}')

compile_po('locale/hi/LC_MESSAGES/django.po', 'locale/hi/LC_MESSAGES/django.mo')
