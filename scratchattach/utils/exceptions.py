# Authentication / Authorization:

class Unauthenticated(Exception):
    """
    Raised when a method that requires a login / session is called on an object that wasn't created with a session.

    If you create Project, Studio, or User objects using :meth:`scratchattach.get_project`, :meth:`scratchattach.get_studio`, or :meth:`scratchattach.get_user`, they cannot be used for actions that require authentication. Instead, use the following methods to ensure the objects are connected to an authenticated session:
    
    - :meth:`scratchattach.Session.connect_project`
    
    - :meth:`scratchattach.Session.connect_user`
    
    - :meth:`scratchattach.Session.connect_studio`

    This also applies to cloud variables, forum topics, and forum posts.
    """

    def __init__(self, message=""):
        self.message = "No login / session connected.\n\nThe object on which the method was called was created using scratchattach.get_xyz()\nUse session.connect_xyz() instead (xyz is a placeholder for user / project / cloud / ...).\n\nMore information: https://scratchattach.readthedocs.io/en/latest/scratchattach.html#scratchattach.utils.exceptions.Unauthenticated"
        super().__init__(self.message)
    pass


class Unauthorized(Exception):
    """
    Raised when an action is performed that the user associated with the session that the object was created with is not allowed to do.

    Example: Changing the "about me" of other users will raise this error.
    """

    def __init__(self, message=""):
        self.message = "The user corresponding to the connected login / session is not allowed to perform this action."
        super().__init__(self.message)

    pass

class XTokenError(Exception):
    """
    Raised when an action can't be performed because there is no XToken available.

    This error can occur if the xtoken couldn't be fetched when the session was created. Some actions (like loving projects) require providing this token.
    """

    pass

# Not found errors:

class UserNotFound(Exception):
    """
    Raised when a non-existent user is requested.
    """

    pass


class ProjectNotFound(Exception):
    """
    Raised when a non-existent project is requested.
    """

    pass

class ClassroomNotFound(Exception):
    """
    Raised when a non-existent Classroom is requested.
    """

    pass


class StudioNotFound(Exception):
    """
    Raised when a non-existent studio is requested.
    """

    pass

class ForumContentNotFound(Exception):
    """
    Raised when a non-existent forum topic / post is requested.
    """
    pass

class CommentNotFound(Exception):
    pass

# API errors:

class LoginFailure(Exception):
    """
    Raised when the Scratch server doesn't respond with a session id.

    This could be caused by an invalid username / password. Another cause could be that your IP address was banned from logging in to Scratch. If you're using an online IDE (like replit), try running the code on your computer.
    """

    pass

class FetchError(Exception):
    """
    Raised when getting information from the Scratch API fails. This can have various reasons. Make sure all provided arguments are valid.
    """

    pass

class BadRequest(Exception):
    """
    Raised when the Scratch API responds with a "Bad Request" error message. This can have various reasons. Make sure all provided arguments are valid.
    """

    pass


class Response429(Exception):
    """
    Raised when the Scratch API responds with a 429 error. This means that your network was ratelimited or blocked by Scratch. If you're using an online IDE (like replit.com), try running the code on your computer.
    """

    pass

class CommentPostFailure(Exception):
    """
    Raised when a comment fails to post. This can have various reasons.
    """

    pass

class APIError(Exception):
    """
    For API errors that can't be classified into one of the above errors
    """
    pass

class ScrapeError(Exception):
    """
    Raised when something goes wrong while web-scraping a page with bs4.
    """

    pass

# Cloud / encoding errors:

class ConnectionError(Exception):
    """
    Raised when connecting to Scratch's cloud server fails. This can have various reasons.
    """

    pass


class InvalidCloudValue(Exception):
    """
    Raised when a cloud variable is set to an invalid value.
    """

    pass


class InvalidDecodeInput(Exception):
    """
    Raised when the built-in decoder :meth:`scratchattach.encoder.Encoding.decode` receives an invalid input.
    """

    pass


# Cloud Requests errors:

class RequestNotFound(Exception):
    """
    Cloud Requests: Raised when a non-existent cloud request is edited using :meth:`scratchattach.cloud_requests.CloudRequests.edit_request`.
    """

    pass

# Websocket server errors:

class WebsocketServerError(Exception):

    """
    Raised when the self-hosted cloud websocket server fails to start.
    """

    pass

class CouldNotUpdateProfileIcon(Exception):
    """
    Raised when there was an error updating the user profile icon
    """
    pass