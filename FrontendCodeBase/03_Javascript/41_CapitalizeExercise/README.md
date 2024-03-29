# Capitalize Exercise

Define a function called capitalize that accepts a string argument and returns a new string with the first letter capitalized<br/>
(but the rest of the string unchanged).<br/>

For example:<br/>

- capitalize('eggplant') // "Eggplant"
- capitalize('pamplemousse') // "Pamplemousse"
- capitalize('squid') //"Squid"

<br/>
## Hints:

- Remember that strings are immutable, meaning that you cannot simply change the first letter in the original string.<br/>You will need to make a new string that you return.

- Single out the first letter and capitalize it. (use a string method to help!)

- Add that first letter to the rest of the original string, sliced to omit the original first letter (use a string method to help!)

- For example: 'eggplant' becomes 'E' + 'ggplant'
