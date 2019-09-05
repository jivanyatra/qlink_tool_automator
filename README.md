# qlink_tool_automator
### Purpose
The purpose of this tool is to make our ops dept run a bit more smoothly when programming units.

This tool simulates the following (in order):
1. waiting for any input (to give the user a chance to plug in the device)
1. launching the old tool
1. entering the device pw and connecting to the device
1. opening the raw prompt
1. entering a programming command of choice
   * this includes the password, url, and port
1. providing a two second window for manual verification
1. closing the old tool
1. launching the new tool
1. changing the baud rate for the device and connecting to it
1. opening the raw prompt
1. entering a programming command of choice
   * this includes the password twice, ip address, and port
1. providing a two second window for manual verification
1. closing the new tool
*repeat*

### Source/Collab
I've mainly stuck this code here as a way of re-familiarizing myself with git and to act as part of my portfolio.

The tools used are proprietary, without an automation API. This process turn a two-person error-prone process into a 1 or 2 person less error-prone process.  Manual verification is still required, but balancing two paste buffers is no loner needed, and very little interaction is required.

As such, I'm not looking for collaboration.

### To Do
- [x] Initial build, very basic
- [x] Make sure it runs on windows (via pyinstaller)
- [ ] Make it more modular with an external configuration
- [ ] Find an alternative way of launching the apps without using windows shortcuts.

# Changelog

#### v 0.5.1 - in progress
* adding external configuration files
* adding parser and abstracting away some of the scriptyness into discrete functions

#### v 0.5 - released 08/19/19
* initial version
* basic version, very scripty
* gets the job done with pyinstaller
