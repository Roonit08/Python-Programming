names =['ram','shyam','hari','rita','Ramesh']
# new_names=[new_name for names in new_names if name.lower()=='r']
new_names=[names for names in names if names.lower().startswith('r')]
print(new_names)