# Requirements Document

## Introduction

This feature adds a steel and aluminum business frontend to the existing Django project. The new site shares the same database as the interior design project but presents a completely different UI/theme tailored for a steel and aluminum fabrication/supply business. The system reuses existing Django apps (services, projects, contact, testimonials, team, site_settings, leads) with new templates, static assets, and URL routing — no new database migrations are required.

## Glossary

- **SA_Site**: The steel and aluminum business website (the new frontend)
- **Interior_Site**: The existing interior design website sharing the same Django project and database
- **Project**: A completed or ongoing steel/aluminum fabrication or installation job stored in `apps/projects`
- **Service**: A steel/aluminum business offering stored in `apps/services`
- **Contact_Form**: The inquiry form backed by `apps/contact`
- **Lead**: A sales lead stored in `apps/leads`
- **SiteSettings**: Global contact/social data stored in `apps/site_settings`
- **TeamMember**: A staff record stored in `apps/team`
- **Testimonial**: A client review stored in `apps/testimonials`
- **Admin**: A Django superuser or staff user managing content via the Django admin panel
- **Visitor**: An unauthenticated user browsing the SA_Site

---

## Requirements

### Requirement 1: Home Page

**User Story:** As a Visitor, I want to see a professional home page for the steel and aluminum business, so that I immediately understand what the company offers and can navigate to relevant sections.

#### Acceptance Criteria

1. THE SA_Site SHALL display a hero/banner section with a headline, subheadline, and a call-to-action button on the home page.
2. THE SA_Site SHALL display a "Why Choose Us" or features highlights section on the home page showing key strengths (e.g., quality materials, precision fabrication, on-time delivery).
3. THE SA_Site SHALL display a summary of featured Services fetched from the `apps/services` database on the home page.
4. THE SA_Site SHALL display a summary of featured Projects fetched from `apps/projects` where `is_featured=True` on the home page.
5. THE SA_Site SHALL display a Testimonials section fetched from `apps/testimonials` where `is_active=True` on the home page.
6. THE SA_Site SHALL display a statistics/counter section (e.g., years of experience, projects completed, clients served) on the home page.
7. WHEN a Visitor clicks the call-to-action button on the hero section, THE SA_Site SHALL navigate the Visitor to the Contact page.

---

### Requirement 2: About Page

**User Story:** As a Visitor, I want to learn about the company's background and team, so that I can decide whether to trust them with my steel and aluminum needs.

#### Acceptance Criteria

1. THE SA_Site SHALL display a dedicated About page with a company overview, mission statement, and history section.
2. THE SA_Site SHALL display TeamMember records fetched from `apps/team` where `is_active=True` on the About page.
3. THE SA_Site SHALL display each TeamMember's name, designation, image, and social links on the About page.

---

### Requirement 3: Services Page

**User Story:** As a Visitor, I want to browse all services offered by the steel and aluminum business, so that I can identify which service fits my requirement.

#### Acceptance Criteria

1. THE SA_Site SHALL display a Services listing page showing all Service records from `apps/services`.
2. THE SA_Site SHALL display each Service's title, description, icon, and associated images on the Services listing page.
3. THE SA_Site SHALL display a dedicated Service detail page for each Service showing full details and all ServiceImage records linked to that Service.
4. WHEN a Visitor clicks on a Service card, THE SA_Site SHALL navigate the Visitor to that Service's detail page.

---

### Requirement 4: Projects / Portfolio Page

**User Story:** As a Visitor, I want to view completed and ongoing steel and aluminum projects, so that I can evaluate the company's quality and experience.

#### Acceptance Criteria

1. THE SA_Site SHALL display a Projects listing page showing all Project records from `apps/projects` where `is_active=True`.
2. THE SA_Site SHALL display each Project's title, cover image, category, status, and location on the Projects listing page.
3. THE SA_Site SHALL support filtering Projects by Category on the Projects listing page.
4. THE SA_Site SHALL display a dedicated Project detail page for each Project showing the full description, all gallery images, budget range, and status.
5. WHEN a Visitor clicks on a Project card, THE SA_Site SHALL navigate the Visitor to that Project's detail page.
6. WHEN a Visitor selects a Category filter, THE SA_Site SHALL display only Projects belonging to that Category.

---

### Requirement 5: Contact Page

**User Story:** As a Visitor, I want to send an inquiry to the business, so that I can request a quote or get more information.

#### Acceptance Criteria

1. THE SA_Site SHALL display a Contact page with a form containing fields: name, email, subject, message, and category.
2. WHEN a Visitor submits the Contact_Form with valid data, THE SA_Site SHALL save the submission to the `apps/contact` Contact model and display a success message.
3. IF a Visitor submits the Contact_Form with missing required fields, THEN THE SA_Site SHALL display inline validation errors without saving the record.
4. THE SA_Site SHALL display the business's phone number, email address, and physical address on the Contact page, fetched from SiteSettings.
5. THE Contact_Form SHALL include a category field with steel/aluminum-relevant options: General Inquiry, Pricing, Custom Fabrication, Complaint.

---

### Requirement 6: Leads / Quote Request

**User Story:** As a Visitor, I want to submit a quote request, so that a sales representative can follow up with me.

#### Acceptance Criteria

1. THE SA_Site SHALL display a "Request a Quote" form accessible from the home page and the Services page.
2. WHEN a Visitor submits the quote form with valid data (name, email, phone, description), THE SA_Site SHALL save a Lead record to `apps/leads` with `status='new'` and display a confirmation message.
3. IF a Visitor submits the quote form with missing required fields, THEN THE SA_Site SHALL display inline validation errors without saving the record.

---

### Requirement 7: UI Theme and Branding

**User Story:** As a business owner, I want the SA_Site to look completely different from the Interior_Site, so that visitors immediately recognise it as a steel and aluminum business.

#### Acceptance Criteria

1. THE SA_Site SHALL use an industrial color palette (e.g., steel grey, metallic silver, dark charcoal, accent orange or yellow) distinct from the Interior_Site's color scheme.
2. THE SA_Site SHALL use a separate set of HTML templates stored under a dedicated template directory (e.g., `templates/steel/`) so that Interior_Site templates are not affected.
3. THE SA_Site SHALL use separate static files (CSS, JS, images) stored under a dedicated static directory (e.g., `static/steel/`) so that Interior_Site static files are not affected.
4. THE SA_Site SHALL display steel and aluminum industry-specific imagery, icons, and copy throughout all pages.
5. THE SA_Site SHALL display a navigation bar with links to: Home, About, Services, Projects, Contact, and Request a Quote.
6. THE SA_Site SHALL display a footer with business contact details, social media links, and quick navigation links, all fetched from SiteSettings.

---

### Requirement 8: Shared Database Compatibility

**User Story:** As a developer, I want the SA_Site to read from and write to the same database as the Interior_Site, so that a single Admin panel manages content for both sites.

#### Acceptance Criteria

1. THE SA_Site SHALL read Service, Project, Testimonial, TeamMember, SiteSettings, Contact, and Lead records from the existing shared database without requiring new migrations.
2. THE SA_Site SHALL use Django's URL routing (separate URL prefix or separate `urls.py` inclusion) to serve SA_Site pages independently from Interior_Site pages.
3. WHEN an Admin updates a Service or Project record in the Django admin panel, THE SA_Site SHALL reflect the updated content on the next page load.
4. WHERE the Admin requires steel/aluminum-specific categories for Projects or Services, THE Admin SHALL manage them through the existing Django admin interface without code changes.

---

### Requirement 9: SEO and Meta Tags

**User Story:** As a business owner, I want each page to have relevant meta tags, so that the site ranks well in search engines for steel and aluminum queries.

#### Acceptance Criteria

1. THE SA_Site SHALL include a unique `<title>` tag on each page reflecting the page's content and the business name.
2. THE SA_Site SHALL include a `<meta name="description">` tag on each page with a relevant description.
3. THE SA_Site SHALL include Open Graph meta tags (`og:title`, `og:description`, `og:image`) on the Home, Services, and Projects pages.

---

### Requirement 10: Responsive Design

**User Story:** As a Visitor using a mobile device, I want the SA_Site to display correctly on all screen sizes, so that I can browse comfortably on any device.

#### Acceptance Criteria

1. THE SA_Site SHALL render all pages correctly on viewport widths from 320px to 1920px.
2. THE SA_Site SHALL display a collapsible mobile navigation menu on viewports narrower than 768px.
3. THE SA_Site SHALL display project and service cards in a single-column layout on viewports narrower than 576px and in a multi-column grid on wider viewports.
