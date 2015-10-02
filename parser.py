# a file to parse a list of potential maxims
# as part of a project to verify their eligibility

fileName = "tests.csv";
maxims = [];
obligations = [];
prohibitions = [];
permissions = [];

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

	# assess maxim
	# assume maxims are in the form 'X must do A', 
	# 'X should not do A', etc
	
	# assess obligation
	if (' must ' in maxim) {
		if (!(' must not ' in maxim)) {
			obliged = true;
		}
	}

	if (' should ' in maxim) {
		if (!(' should not ' in maxim)) {
			obliged = true;
		}
	}

	# assess prohibition
	if (' must not ' in maxim) {
		prohibited = true;
	}

	if (' should not ' in maxim) {
		prohibited = true;
	}

	# check status of maxim
	if (obliged) {
		obligations.append(maxim);
	}

	else if (prohibited) {
		prohibitions.append(maxim);
	}

	else if (!(obliged) && !(prohibited))
		permissions.append(maxim);
	}
}
