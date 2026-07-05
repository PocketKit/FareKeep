import os
import glob

# 1. Update existing HTML files with FAQ links
html_files = ["index.html", "privacy.html", "terms.html", "coming-soon.html", "404.html"]

for f in html_files:
    if not os.path.exists(f): continue
    with open(f, "r") as file:
        content = file.read()
    
    # Update Nav
    if '<li class="nav-item"><a class="nav-link me-lg-3" href="/terms.html">Terms of Service</a></li>' in content:
        if 'FAQ</a></li>' not in content:
            content = content.replace(
                '<li class="nav-item"><a class="nav-link me-lg-3" href="/terms.html">Terms of Service</a></li>',
                '<li class="nav-item"><a class="nav-link me-lg-3" href="/terms.html">Terms of Service</a></li>\n                        <li class="nav-item"><a class="nav-link me-lg-3" href="/faq.html">FAQ</a></li>'
            )
    elif '<li class="nav-item"><a class="nav-link me-lg-3" href="terms.html">Terms of Service</a></li>' in content:
        if 'FAQ</a></li>' not in content:
            content = content.replace(
                '<li class="nav-item"><a class="nav-link me-lg-3" href="terms.html">Terms of Service</a></li>',
                '<li class="nav-item"><a class="nav-link me-lg-3" href="terms.html">Terms of Service</a></li>\n                        <li class="nav-item"><a class="nav-link me-lg-3" href="faq.html">FAQ</a></li>'
            )
            
    # Update Footer
    if '<a href="/terms.html">Terms</a>' in content:
        if 'FAQ</a>' not in content:
            content = content.replace(
                '<a href="/terms.html">Terms</a>',
                '<a href="/terms.html">Terms</a>\n                    <span class="mx-1">&middot;</span>\n                    <a href="/faq.html">FAQ</a>'
            )
    elif '<a href="terms.html">Terms</a>' in content:
        if 'FAQ</a>' not in content:
            content = content.replace(
                '<a href="terms.html">Terms</a>',
                '<a href="terms.html">Terms</a>\n                    <span class="mx-1">&middot;</span>\n                    <a href="faq.html">FAQ</a>'
            )
            
    with open(f, "w") as file:
        file.write(content)


# 2. Create HTML wrapper generation function
def generate_html(md_filename, output_filename, is_nested=False):
    title = md_filename.replace(".md", "").replace("_", " ").title() + " - FAQ"
    
    # We will use absolute paths to ensure robustness.
    
    if is_nested:
        md_fetch_path = md_filename
    else:
        md_fetch_path = md_filename

    html_template = f"""<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <title>{title} — FareKeep</title>
        <link rel="icon" type="image/x-icon" href="/assets/favicon.ico" />
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" rel="stylesheet" />
        <link rel="preconnect" href="https://fonts.gstatic.com" />
        <link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,wght@0,600;1,600&amp;display=swap" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css2?family=Mulish:ital,wght@0,300;0,500;0,600;0,700;1,300;1,500;1,600;1,700&amp;display=swap" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css2?family=Kanit:ital,wght@0,400;1,400&amp;display=swap" rel="stylesheet" />
        <link href="/css/styles.css" rel="stylesheet" />
        <!-- Marked.js for markdown rendering -->
        <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
        <style>
            #markdown-content h1, #markdown-content h2, #markdown-content h3 {{
                font-family: 'Newsreader', serif;
                margin-top: 1.5rem;
                margin-bottom: 1rem;
            }}
            #markdown-content p, #markdown-content li {{
                font-family: 'Mulish', sans-serif;
                color: #6c757d;
                line-height: 1.7;
            }}
            /* Ensure links look good */
            #markdown-content a {{
                color: #1976D2;
                text-decoration: none;
            }}
            #markdown-content a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body id="page-top" class="d-flex flex-column min-vh-100 bg-light">
        <!-- Navigation-->
        <nav class="navbar navbar-expand-lg navbar-light shadow-sm bg-white" id="mainNav">
            <div class="container px-5">
                <a class="navbar-brand fw-bold d-flex align-items-center" href="/index.html">
                    <img src="/assets/img/app_icon.png" alt="FareKeep Logo" height="30" class="me-2" style="border-radius: 6px;">
                    FareKeep
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                    Menu
                    <i class="bi-list"></i>
                </button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav ms-auto me-4 my-3 my-lg-0">
                        <li class="nav-item"><a class="nav-link me-lg-3" href="/index.html#features">Features</a></li>
                        <li class="nav-item"><a class="nav-link me-lg-3" href="/index.html#download">Download</a></li>
                        <li class="nav-item"><a class="nav-link me-lg-3" href="/privacy.html">Privacy Policy</a></li>
                        <li class="nav-item"><a class="nav-link me-lg-3" href="/terms.html">Terms of Service</a></li>
                        <li class="nav-item"><a class="nav-link me-lg-3 active" href="/faq.html">FAQ</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        
        <!-- Content -->
        <section class="py-5 flex-grow-1">
            <div class="container px-5 my-5">
                <div class="row justify-content-center">
                    <div class="col-lg-8" id="markdown-content">
                        <!-- Markdown content will be loaded here -->
                        <div class="text-center">
                            <div class="spinner-border text-primary" role="status">
                                <span class="visually-hidden">Loading...</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Footer-->
        <footer class="bg-black text-center py-5 mt-auto">
            <div class="container px-5">
                <div class="text-white-50 small">
                    <div class="mb-2">&copy; FareKeep 2026. All Rights Reserved.</div>
                    <a href="/privacy.html">Privacy</a>
                    <span class="mx-1">&middot;</span>
                    <a href="/terms.html">Terms</a>
                    <span class="mx-1">&middot;</span>
                    <a href="/faq.html">FAQ</a>
                </div>
            </div>
        </footer>

        <!-- Bootstrap core JS-->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
        <!-- Markdown loading script -->
        <script>
            fetch("{md_fetch_path}")
                .then(response => {{
                    if (!response.ok) throw new Error("File not found");
                    return response.text();
                }})
                .then(text => {{
                    // Rewrite .md links to .html so that cross-linking between FAQs works
                    text = text.replace(/href="([^"]+)\.md"/g, 'href="$1.html"');
                    text = text.replace(/\]\(([^)]+)\.md\)/g, ']($1.html)');
                    document.getElementById('markdown-content').innerHTML = marked.parse(text);
                }})
                .catch(error => {{
                    document.getElementById('markdown-content').innerHTML = '<p class="text-danger">Error loading content.</p>';
                    console.error('Error loading markdown:', error);
                }});
        </script>
    </body>
</html>"""
    
    with open(output_filename, "w") as f:
        f.write(html_template)
    print(f"Created {output_filename}")


# 3. Create faq.html in root
if os.path.exists("faq.md"):
    generate_html("faq.md", "faq.html", is_nested=False)
else:
    print("No faq.md found in root.")

# 4. Create html wrappers for each .md in faq/
if os.path.exists("faq"):
    md_files = glob.glob("faq/*.md")
    for md_file in md_files:
        filename = os.path.basename(md_file)
        html_file = os.path.join("faq", filename.replace(".md", ".html"))
        generate_html(filename, html_file, is_nested=True)
else:
    print("No faq directory found.")

print("Done.")
