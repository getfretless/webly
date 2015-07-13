#!/usr/bin/env ruby
require 'cgi'
cgi = CGI.new
page = 'Welcome'
page = cgi['page'] unless cgi['page'].empty?

puts cgi.header

greetings = ['Mr. President', 'Your Royal Majesty', 'Your Highness']
if cgi['name'].empty?
  greeting = greetings.sample
else
  greeting = cgi['name']
end

html_head = "<html>
  <head>
    <title>#{page}</title>
  </head>
  <body>"

html_foot = "</body></html>"

if page == 'about'
  puts "#{html_head}Hey, #{greeting}. Let me tell you about us. We are coders!#{html_foot}"
else
  puts "#{html_head}Hello, #{greeting}!#{html_foot}"
end
