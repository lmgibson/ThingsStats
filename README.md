# Overview - ThingsStats

This is a set of tools to analyze your [Things](https://culturedcode.com/things/) data. It is currently a work in progress but some goals are to generate reports that tell you how many tasks you have completed, how many you have uncompleted, and break it down further by project. Additionally, the tools will allow you to see your oldest outstanding tasks and maybe(!) search through them based on notes or title descriptions.

# How To Use

To get data from the past week or month you can type: `python ./path/to/folder/getDateData.py 'week'` where the argument can be either 'week' or 'month'. This will dump a file onto your desktop that contains a list of tasks within the past week or month by date and title.

Alternatively, if you want to get a report on your task stats for the past week or month you can use: `python ./path/to/folder/report.py`. This is a work in progress so it will just give you some summary stats over the past month.
