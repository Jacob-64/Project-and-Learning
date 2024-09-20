
## **Cypher Substitiution with Rotational Shft.py**

### **Overview**
This Python script implements a custom cipher mechanism to decrypt or transform a given message by rotating the characters in the "inner" key based on a defined mapping. It's useful for CTF challenges where deciphering an encoded message is necessary.

### **Script Breakdown**
1. **Imports**
   ```python
   import string
   from collections import deque
   ```
   - The script imports the `string` module to access uppercase letters, and `deque` from `collections` to manipulate the inner key with efficient rotations.

2. **Key Definition**
   ```python
   outer = string.ascii_uppercase + "{}"
   inner = deque("COSDHG{QNFUVWLEZYXPTKMR}ABJI")
   ```
   - The `outer` variable contains the uppercase alphabet along with the curly braces `{}` to match the expected characters.
   - The `inner` deque is a scrambled version of the `outer` key that will be rotated for decryption or encryption.

3. **Message Definition**
   ```python
   msg = "e0261e3f44788a669ff87710eb149eba87a9b7ce2abb92b45e862de035485ad02aff59e980e5b0db1657332f202bebb0..."
   ```
   - The `msg` variable holds an encrypted message. This message is presumably encoded using the custom cipher mechanism.

4. **Cipher Rotation Logic**
   ```python
   for rotation in range(len(outer)):
       inner.rotate(rotation)
       lookup = dict(zip(outer, inner))
       print("".join(lookup[c] for c in msg))
   ```
   - The script rotates the `inner` deque for every possible position and maps the characters of the `outer` string to the `inner` string using a dictionary.
   - It attempts to decrypt the message by checking all rotations and printing the result for each one.

### **Potential Use Case**
This script could be used in CTF competitions to brute-force or solve rotational ciphers where each rotation of the inner key results in a different mapping of the encrypted message.

### **How to Use**
1. Clone the repository containing this script:
   ```bash
   git clone https://github.com/username/repo_name
   ```
2. Navigate to the repository folder:
   ```bash
   cd repo_name
   ```
3. Run the script using Python:
   ```bash
   python3 CTF_Cypher.py
   ```
4. The output will display different potential decryptions of the encoded message for each key rotation.

### **Notes**
- This script assumes that the encrypted message (`msg`) only contains characters present in the `outer` string (uppercase letters and curly braces `{}`).
- To use this script with a different message, replace the `msg` variable with your encoded string.
- **Optimization Note:** If the original encoding pattern is known (e.g., the number of rotations), adjusting the script to only try specific rotations could improve performance.

### **Type of Cipher**
This script implements a **custom substitution cipher** that blends a **monoalphabetic substitution** cipher with **rotational shifts** similar to a Caesar cipher. The custom `inner` key is rotated for each iteration, making this a unique hybrid of substitution and rotation.

---

You can paste this directly into the `README.md` file or as part of your repository's documentation. Let me know if you'd like any additional customization!
