import json
import re

# Step 1: Read the template.html file
with open('./_template.html', 'r') as file:
    template = file.read()

# Step 2: Load cities.json
with open('./_all_cities.json', 'r') as file:
    cities = json.load(file)

# Step 3: Create new HTML files and collect URLs for sitemap
urls = []

for entry in cities:
    city = entry['city']
    country = entry['country']
    city_underscore = re.sub(r'\s+', '_', country.lower()) + '_' + re.sub(r'\s+', '_', city.lower())

    # Replace placeholders in the template
    new_content = template.replace('$CITY', city).replace('$COUNTRY', country)

    # Save the new HTML file
    new_filename = f'./{city_underscore}.html'
    with open(new_filename, 'w') as new_file:
        new_file.write(new_content)

    # Collect the URL for sitemap
    url = f'https://wooh.app/{city_underscore}'
    urls.append(url)

# Step 4: Update sitemap.xml
sitemap_header = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1" xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">
    <url>
        <loc>https://wooh.app/</loc>
        <priority>1.0</priority>
        <changefreq>monthly</changefreq>
    </url>
    <url>
        <loc>https://wooh.app/policy</loc>
        <priority>1.0</priority>
        <changefreq>monthly</changefreq>
    </url>
    <url>
        <loc>https://wooh.app/terms</loc>
        <priority>1.0</priority>
        <changefreq>monthly</changefreq>
    </url>
    <url>
        <loc>https://wooh.app/delete_account</loc>
        <priority>0.5</priority>
        <changefreq>monthly</changefreq>
    </url>'''
sitemap_footer = '''
</urlset>'''

# Add new city URLs
sitemap_urls = ''
for url in urls:
    sitemap_urls += f'''
    <url>
        <loc>{url}</loc>
        <priority>0.9</priority>
        <changefreq>monthly</changefreq>
    </url>'''

# Combine parts and save sitemap.xml
sitemap_content = sitemap_header + sitemap_urls + sitemap_footer
with open('./sitemap.xml', 'w') as sitemap_file:
    sitemap_file.write(sitemap_content)

print("HTML files and sitemap.xml have been created successfully.")
