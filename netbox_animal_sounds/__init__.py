from extras.plugins import PluginConfig


class AnimalSoundsConfig(PluginConfig):
    """
    This class defines attributes for the NetBox Animal Sounds plugin.
    """
    # Plugin package name
    name = 'netbox_animal_sounds'

    # Human-friendly name and description
    verbose_name = 'Animal Sounds'
    description = 'Example NetBox plugin'

    # Plugin version
    version = '0.1'

    # Plugin author
    author = 'Jeremy Stretch'

    # Configuration parameters that MUST be defined by the user (if any)
    required_settings = []

    # Default configuration parameter values, if not set by the user
    default_settings = {
        'loud': True
    }

    # Base URL path. If not set, the plugin name will be used.
    base_url = 'animal-sounds'

