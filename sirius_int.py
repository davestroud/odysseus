# Libraries Included:
# Numpy, Scipy, Scikit, Pandas


# print("Hello World")

"""
Let us suppose you are working for a healthcare company. Congratulations!

The company you're working at is trying to grow and scale its ability to provide medications to users, without requiring a human to perform the validation checks. And since you're the new Engineer on the team, they want you to step in! So the problem is the following: you have been provided a list of medications (compiled by several pharmacists) that tell you medications that should not be prescribed together to a single customer.

Below is a sample of the information provided to you as a csv input:

Medications, Reason
a|b, can cause rashes
c|d, can cause stomach issues
g|h, can cause nausea
As such, they want you to go through a list of patient subscriptions, where each line represents a single patient's medications, where each line depicts a single patient's prescriptions

a, h, d, x
b, c
b, g, h
z, x, y, a, b
and process each line as a separate input, and return whether the medication is okay to process, or whether there is an issue with the medication, in which case, you would need to specify the cause for the issue.

"""



# TODO: Complete the construction of medications to avoid
medications_to_avoid = {

"a|b": "can cause rashes",
"c|d": "can cause stomach issues",
"g|h": "can cause nausea"

}

def validate_medications(subscription):
    # This function would validate the subscription and return a list of potential issues
    # Their code down here:
    # subscription = ["a","b","c"]
    
    issues = []

    for k, v in medications_to_avoid.items():
        # if k == ###
        # k = "a|b"
        # v = "can cause rashes"
        k_string = k.split("|")
        k_0 = k_string[0]
        k_1 = k_string[1]
        
        if k_0 in subscription and k_1 in subscription:
            issues.append(v)
        
        # "a|b"[0][1]
        
        # If k "ab" and char of [list 1] can cause rash
        # if k gh and char of [list 2] can cause stomach issuse and nausia
    
    return issues 

if __name__ == "__main__":
    medications = [
        ["a", "b", "c"], #[can cause rashes]
        ["d", "h", "g", "c"] #  [can cause stomach issues, can cause nausea]
    ]

    for medication in medications:
        issues = validate_medications(medication)

        if issues:
            # print(f"There are issues with the subscription: {', '.join(medication)}")
            for issue in issues:
                print(issue)
            print()
        else:
            print("No issues found with the subscription.")

