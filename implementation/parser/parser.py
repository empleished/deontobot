#TODO formal parser

# a file to parse a list of potential maxims
# as part of a project to verify their eligibility

fileName = "tests.csv";
maxims = [];
obligations = {}; # key: integer lookup (conditions), value: list
prohibitions = {}; # key: integer lookup (conditions), value: list
permissions = {}; # key: integer lookup (conditions), value: list
conditions = []; # list of lists

# open file
file = open(fileName, 'r');

# read file
for (line in file) {
	maxims.append(line);
}

# close file
file.close();

# sort into obligations/prohibitions
for (maxim in maxims) {
	obliged = false;
	prohibited = false;

	# check condition
	conditionList = [];
	conditionID = 0;

	#TODO parse conditions somehow???
	
	#TODO add conditions
	if (!(conditionList in conditions)) {
		conditions.append(conditionList);
	}

	# find location of conditionList in conditions
	i = 0;

	while (i < conditions.length) {
		if (conditions[i] == conditionList) {
			conditionID = i;
		}
	}

	#TODO split actions out from maxims
	action = [];

	# assess action
	# assume maxims are in the form 'X must do A', 
	# 'X should not do A', etc
	
	# assess obligation
	#TODO change to append to key: conditionID
	if (' must ' in action) {
		if (!(' must not ' in action)) {
			obliged = true;
		}
	}

	if (' should ' in action) {
		if (!(' should not ' in action)) {
			obliged = true;
		}
	}

	# assess prohibition
	if (' must not ' in action) {
		prohibited = true;
	}

	if (' should not ' in maxim) {
		prohibited = true;
	}

	# check status of maxim
	if (obliged) {
		obligations.append(action);
	}

	else if (prohibited) {
		prohibitions.append(action);
	}

	else if (!(obliged) && !(prohibited))
		permissions.append(action);
	}
}

#TODO take the lists and convert them into facts


