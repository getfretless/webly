#!/usr/bin/env ruby
require 'cgi'
cgi = CGI.new
page = 'home'
page = cgi['page'] unless cgi['page'].empty?
title = {
  'home'  => 'Welcome',
  'about' => 'About Us'
}

puts cgi.header

greetings = ['Mr. President', 'Your Royal Majesty', 'Your Highness']
if cgi['name'].empty?
  greeting = greetings.sample
else
  greeting = cgi['name']
end

html_head = "<html>
  <head>
    <title>Webly: #{title[page.downcase]}</title>
  </head>
  <body>"

html_foot = "</body></html>"

if page.downcase == 'about'
  puts "#{html_head}Hey, #{greeting}. Let me tell you about us. We are coders!#{html_foot}"
else
  puts "#{html_head}Hello, #{greeting}!#{html_foot}"
end
