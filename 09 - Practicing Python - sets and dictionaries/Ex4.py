""" Marina works in the security department of a company and needs to check whether
a specific set of permissions is part of the main permissions of a system. Your
task is to develop a program that receives two lists of permissions and checks
whether the second list is contained in the first.

Input Example:

> CASE 01:
Main permissions: read, write, execute, share
Requested permissions: read, write

> CASE 02:
Main permissions: read, write, execute, share
Requested permissions: read, delete

Expected Output:

> CASE 01:
The requested permissions are part of the main permissions.

> CASE 02:
The requested permissions are not part of the main permissions. """

main_permission = set(p.strip()
                      for p in input("Main permissions: ").lower().split(','))
req_permission = set(
    p.strip() for p in input("Requested permissions: ").lower().split(',')
)

is_subset = req_permission.issubset(main_permission)

if is_subset:
    print("The requested permissions are part of the main permission.")
else:
    print("The requested permissions are not part of the main permission.")
