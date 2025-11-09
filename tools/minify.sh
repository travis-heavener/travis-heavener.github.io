#!/bin/bash
find docs -type f -name "*.css" -exec rm {} \;
rmdir docs/css
find docs -type f -name "*.js" -exec terser {} -o {} \;
find docs -type f -name "*.html" -exec html-minifier-terser {} -o {} \
    --collapse-whitespace --remove-comments --minify-css --use-short-doctype \;
echo "✅ Minify"