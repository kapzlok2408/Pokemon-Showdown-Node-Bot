/*
 *	
 */
exports.id = "custom";

var TypeChart = require('./../typechart.js');
var Calc = require('./../calc.js');
var Data = require('./../battle-data.js');
const fs = require('fs'); //for writing to file
const { spawn } = require('child_process');//for starting python
var wait = require('wait-for-stuff');//utilizes to wait for python file to return action
let { PythonShell } = require('python-shell');//to execute python script

var Pokemon = Calc.Pokemon;
var Conditions = Calc.Conditions;
var dataFileName = "/home/alex/Pokemon-Showdown-Node-Bot/features/battle/battle-ai/modules/rldata.json";
//^used to exchange data between python and nodejs

exports.decide = function (battle, decisions) {
	storeDataToFile(battle, decisions);
	info("stillhere");
	startPython();

	wait.for.condition(
		()=>{return isActionEnteredInFile();}
	);//next statement is executed after wait

	//return decisions[Math.floor(Math.random() * decisions.length)];//return random for debugging purposes
	return decisions[readActionFromFile()];//return action from python gym
};

//returns null; Stores data to JSON for use by python gym
function storeDataToFile(battle, decisions) {
	//reads current JSON, modifies accordingly
	var data = JSON.parse(fs.readFileSync(dataFileName));
	data.battleDecisions = decisions;
	data.battleData = battle;
	data.actionReturned = false;
	//data.pythonStarted = false;//erase please
	data.action = null;
	//writes to file
	fs.writeFileSync(
		dataFileName, 
		JSON.stringify(data), 
		'utf8'
	);
}

//returns boolean; checks if python is done processing and has returned an action
function isActionEnteredInFile() {
	var data = JSON.parse(fs.readFileSync(dataFileName));
	return data.actionReturned;
}

//returns int; returns the index of the decision from the decisions array in exports.decide
function readActionFromFile() {
	var data = JSON.parse(fs.readFileSync(dataFileName));
	return data.action;

}

//returns null; starts the python gym script
function startPython() {

	var data = JSON.parse(fs.readFileSync(dataFileName));

	//should only do something if process has not been started, i.e. first module call in a battle
	//otherwise, do nothing
	if (!data.pythonStarted) {
		data.pythonStarted = true;
		fs.writeFileSync(
			dataFileName,
			JSON.stringify(data),
			'utf8'
		);

		//run the python agent.py and logs errors and results if any
		PythonShell.run(
			'/home/alex/Pokemon-Showdown-Node-Bot/agent.py', 
			null, 
			function (err, results) {
				if (err) {
					error(err);
				} else {
					info(results);
				}
			}
		);
	}
}