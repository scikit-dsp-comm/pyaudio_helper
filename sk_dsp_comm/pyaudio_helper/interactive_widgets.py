import warnings
try:
    from ipywidgets import interactive
    from ipywidgets import ToggleButton
    from ipywidgets import HBox, VBox
    from ipywidgets import Output
except ImportError:
    warnings.warn("Please install ipywidgets for full functionality", ImportWarning)


class InteractiveWidgets():
    """
    Use this class to bind start/stop interactivity to an existing class.
    Set start_handler, and stop_handler with functions for the button handlers to call, then call
    :func:`InteractiveWidgets.create_interactive_widgets` to get started.
    """

    def __init__(self):
        """
        To be safe, all objects will be left blank in major version 1.x.x on init.
        """
        self.start_streaming_button = None
        self.stop_streaming_button = None
        self.streaming_state_indicator = None
        self.streaming_state = False
        self.start_handler = None
        self.stop_handler = None
        self.output_area = None
        self.display_holder = None

    def create_interactive_widgets(self, start_handler, stop_handler):
        """
        This method will create the necessary ipywidget objects and return the final Box to display.
        :return:
        """
        self.start_streaming_button = ToggleButton(
            description='Start Streaming',
            value=False,
            disabled=False,
            button_style='',
            tooltip='Start Streaming',
            icon='play'  # (FontAwesome names without the `fa-` prefix)
        )
        self.stop_streaming_button = ToggleButton(
            description='Stop Streaming',
            value=True,
            disabled=False,
            button_style='',
            tooltip='Stop Streaming',
            icon='stop'  # (FontAwesome names without the `fa-` prefix)
        )
        self.output_area = Output()
        self.start_handler = start_handler
        self.stop_handler = stop_handler
        self.start_streaming_button.observe(self.start_streaming_button_handler)
        self.stop_streaming_button.observe(self.stop_streaming_button_handler)
        self.display_holder = VBox([HBox([self.start_streaming_button, self.stop_streaming_button]), self.output_area])
        return self.display_holder

    def start_streaming_button_handler(self, change):
        """
        Use this handler to bind the start button.
        Disable the start button on click, and set the stop button to False.
        :return:
        """
        if change['new']:
            self.output_area.clear_output()
            self.start_streaming_button.disabled = True
            self.stop_streaming_button.value = False
            with self.output_area:
                self.start_handler()

    def stop_streaming_button_handler(self, change):
        """
        Use this handler to bind the stop button.
        Re-enable the start button on click, and set the stop button to False.
        :param change:
        :return:
        """
        if change['new'] == True:  # This is required because otherwise this will trigger true on dicts/other objects
            self.start_streaming_button.value = False
            self.start_streaming_button.disabled = False
            with self.output_area:
                self.stop_handler()

    def set_stopped_state(self):
        self.start_streaming_button.value = False
        self.start_streaming_button.disabled = False
        self.stop_streaming_button.value = True
