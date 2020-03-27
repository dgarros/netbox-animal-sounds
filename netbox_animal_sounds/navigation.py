from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


# Declare a list of menu items to be added to NetBox's built-in naivgation menu
menu_items = (

    # Each PluginMenuItem instance renders a custom menu item. Each item may have zero or more buttons.
    PluginMenuItem(
        link='plugins:netbox_animal_sounds:list_animals',
        link_text='List all animals',
        permissions=[],
        buttons=(

            # Add a default button which links to the random animal view
            PluginMenuButton(
                link='plugins:netbox_animal_sounds:random_animal',
                title='Random animal',
                icon_class='fa-question'
            ),

            # Add a green button which links to the admin view to add a new animal. This
            # button will appear only if the user has the "add_animal" permission.
            PluginMenuButton(
                link='admin:netbox_animal_sounds_animal_add',
                title='Add a new animal',
                icon_class='fa-plus',
                color=ButtonColorChoices.GREEN,
                permissions=['netbox_animal_sounds.add_animal']
            ),
        )
    ),

)

