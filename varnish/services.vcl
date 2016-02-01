vcl 4.0;

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

  return (hash);
}
