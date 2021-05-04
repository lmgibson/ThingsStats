# Overview - ThingsStats

A command line tool for [Things](https://culturedcode.com/things/). The tool has a functionality to add checklist items to a daily todo (`things add`) and interactive reporting to explore incomplete tasks (`things report`).

# How To Use

1. Install with: `pip install thingscli`
2. Type `things` to see a list of commands. Currently support add and report.
3. Type `things report` to access the interactive reporting functionality.

# Commands

## add

Add is a command that creates a daily todo and can add checklist items to it. For example, `things add 'hello'` will create a todo of the format "weekday mm/dd/yyyy" and a checklist item with the title 'hello'. Currently it will only do this if there is a project titled 'Daily Tracker'.

Personally, I use this to support my own workflow of adding tasks as they come up to a daily todo.

Example coming soon.

## report

Report is an interactive tool that presents the user with different information on their things usage.

[![asciicast](https://asciinema.org/a/qYOWzmVNsiahVvCgfhdD0w5Ps.png)](hhttps://asciinema.org/a/qYOWzmVNsiahVvCgfhdD0w5Ps)
