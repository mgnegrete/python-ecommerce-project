from oscar.apps.catalogue.models import *


#create the sizes attributes

size = AttributeOptionGroup.objects.create(name='size')
color = AttributeOptionGroup.objects.create(name='color')


AttributeOption.objects.create(
    group= size,
    option = 'Small'
)
AttributeOption.objects.create(
    group= size,
    option = 'Medium'
)
AttributeOption.objects.create(
    group= size,
    option = 'Large'
)
AttributeOption.objects.create(
    group= size,
    option = 'X-Large'
)

# Assign option to color option group

AttributeOption.objects.create(
    group= color,
    option = 'Black'
)
AttributeOption.objects.create(
    group= color,
    option = 'White'
)
AttributeOption.objects.create(
    group= color,
    option = 'Scarlet Red'
)


#optional feedback
print("AttributeOption group and Attribute option added")