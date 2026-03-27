#!/usr/bin/env bash
find public -type f -name "*.css" -exec rm {} \;
rmdir public/css
find public -type f -name "*.js" -exec terser {} -o {} \;
find public -type f -name "*.html" -exec html-minifier-terser {} -o {} \
    --collapse-whitespace --remove-comments --minify-css --use-short-doctype \;
echo "✅ Minify"