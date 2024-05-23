# Use Hugo extended image
FROM registry.gitlab.com/pages/hugo/hugo_extended:latest

# Install necessary tools
RUN apk add --no-cache git go npm brotli

# Set work directory
#ADD . /site
WORKDIR /site

# Copy your Hugo site into the Docker image
#COPY . /site

# Set Git to trust the repository in this directory
RUN git config --global --add safe.directory /site

# Install Node.js packages
RUN npm install postcss postcss-cli autoprefixer

# Build the site with Hugo
#RUN hugo --minify

# Compress assets
#RUN find public -type f -regex '.*\.\(htm\|html\|txt\|text\|js\|css\|json\)$' -exec brotli -f -k {} \;
#RUN find public -type f -regex '.*\.\(xml\|ttf\|svg\)$' -exec brotli -f -k {} \;

# Expose port 1313 for the Hugo server
EXPOSE 1313

# Define the default command to run Hugo server
CMD ["hugo", "server", "--bind", "0.0.0.0", "--disableFastRender"]
