class Solution:
    def minOperations(self, logs: list[str]) -> int:
        # Store operations to go back to main folder
        operations = 0

        # Iterate through log list
        for operation in logs:
            if operation == "../":
                if operations > 0:
                    operations -= 1
            elif operation != "./":
                operations += 1

        # Return operations count
        return operations
