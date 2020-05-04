# Kitten Proxy

Serves a web page containing a single link to
https://placekitten.com/, picking a random width
and height between configured bounds.

This app can be configured in two ways:

- through environment variables named
  `KITTEN_MIN_WIDTH`, `KITTEN_MAX_WIDTH`,
  `KITTEN_MIN_HEIGHT`, `KITTEN_MAX_HEIGHT`
- if the variable `KITTEN_CONFIG` is set,
  it is expected to be the path to a YAML
  file containing a dictionary with the
  same variables (see the sample configuration
  file in the repo)

If `KITTEN_CONFIG` is set, the configuration
file takes precedence over the variables.

