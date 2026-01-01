class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1  # Initialize carry to 1 for the increment operation
        result = []

        for i in range(len(digits) - 1, -1, -1):
            current_sum = digits[i] + carry
            result.insert(0, current_sum % 10)  # Insert the least significant digit at the beginning
            carry = current_sum // 10  # Update carry for the next iteration

        while carry:
            result.insert(0, carry % 10)  # Insert remaining carry digits
            carry //= 10  # Update carry for any remaining carry digits

        return result