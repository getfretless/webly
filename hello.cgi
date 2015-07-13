#!/usr/bin/env ruby
require 'cgi'
cgi = CGI.new
puts cgi.header

greetings = ['Mr. President', 'Your Royal Majesty', 'Your Highness']
if cgi['name'].empty?
  greeting = greetings.sample
else
  greeting = cgi['name']
end


puts "<html>
  <head>
    <title>My first web page</title>
  </head>
  <body>
    Hello, #{greeting}!
  </body>
</html>"
