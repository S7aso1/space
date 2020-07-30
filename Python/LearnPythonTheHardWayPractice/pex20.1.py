# print('lets practice everything')
# print('you\'d need to know \'bout escapes with \\ that do:')
# print('\n newlines and \t tabs')
#
# poem = """
# \tThe lovely world
# with logic so firmly planted
# cannot discern \n the needs of love
# nor comprehend passion from intuition
# and requires an explanation
# \n\t\twhere there is none.
# """
#
# print ('-------')
# print(poem)
# print('--------')
#
#
# five = 10 - 2 + 3 - 6
# print(f"this should be five {five}")
#

def secret_formula(started):
    jellybeans = start_point * 500
    jars = jellybeans/ 1000
    crates = jars /100
    return jellybeans, jars, crates

start_point = 10000
jellybeans, glassjars, woodencrates = secret_formula(start_point)

#remember this is another way to format a string
print('with a starting point of: {}'.format(start_point))
print(f'with a starting point of: {start_point}')
#its just like with an f"" starting
print(f'we`d have {jellybeans} jellybeans, {glassjars} jars, and {woodencrates} crates')

start_point = start_point / 10

print("we can also do this way:")
formula = secret_formula(start_point)
#this is easy way to apply a list to format a string
print(f'we`d have {jellybeans} jellybeans, {glassjars} jars, and {woodencrates} crates'.format(*formula))
