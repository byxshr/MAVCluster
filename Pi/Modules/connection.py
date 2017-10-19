#  -*- coding: utf-8 -*-

"""
Modules.connection
~~~~~~~~~~~~~~~

Implement the methods for the communication between monitor and drone mainly through TCP connection.
"""
class Connection():
    """Maintain an connection between the drone and monitor."""
    def __init__(self, host, port):
        self.__CID = -1;  # Connection ID used to identify specific the drone while communicating with the monitor.
        self.establish_connection(host, port)

    def establish_connection(self, host, port):
        """
        Once the main process has connected to the drone successfully, this method will be called to initialize the
        drone state in the monitor process, then they should maintain the connection identified by an unique ID till all
        tasks are done and the drone has landed safely.

        Returns:
            One unique ID for the drone compared to other drones in the cluster, which is generated by the monitor.
        """

    def report_to_monitor(self):
        """Report the states of drone to the monitor on time."""

    def hear_from_monitor(self):
        """Deal with instructions sent by monitor.

        Keeping listening to the monitor, once messages arrived this method will start analyzing and translate them into
        the form that other modules can handle.

        Returns: Dictionary that can be parsed by command execution module.
        """

    def close_connection(self):
        """Close the connection that maintained by the instance

        Returns:
            A boolean variable that indicate whether the connection closed sucessfully.
        """