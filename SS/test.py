# symmetryMapNode = {6:2,7:3,8:1}
    
# for new,ref in symmetryMapNode.items():
#     print(new)
#     print(ref)
#     print('33')
    
    
# a = [1,4,3,4,5,6]

# for i,x in enumerate(a):
    
#     print(f'this is i: {i}')
#     print(f'this is x {x}')
    
    
data_dict = {
    1: {'col1': 'data1', 'col2': 'data2', 'col3': 'data3'},
    2: {'col1': 'data4', 'col2': 'data5', 'col3': 'data6'},
    3: {'col1': 'data7', 'col2': 'data8', 'col3': 'data9'}
}

# List of keys to keep
keys_to_keep = [1, 3]

# Create a subset dictionary
subset_dict = {key: data_dict[key] for key in keys_to_keep if key in data_dict}

# Print the result
print(subset_dict)