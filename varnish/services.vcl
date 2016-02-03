vcl 4.0;

// Set up a default backend for varnish to cache
backend default {
  .host = "cars_service";
  .port = "5000";
}

sub vcl_recv {
  // Only cache GET requests
  if (req.method != "GET") {
    return (pass);
  }

  // Don't cache our state endpoint
  if (req.url == "/state") {
    return (pass);
  }

  // Everything else is cached
  return (hash);
}

sub vcl_backend_response {
  // Allow client to specify caching levels w/custom header
  if (bereq.http.ServiceCacheTTL == "short") {
    set beresp.ttl = 2s;
  } else if (bereq.http.ServiceCacheTTL == "long") {
    set beresp.ttl = 30s;
  } else {
    set beresp.ttl = 10s;
  }
}
