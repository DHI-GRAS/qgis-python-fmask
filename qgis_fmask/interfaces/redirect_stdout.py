from contextlib import contextmanager
import functools
import sys


class FeedbackLogger:
    def __init__(self, feedback):
        self.feedback = feedback

    def write(self, msg):
        self.feedback.pushConsoleInfo(msg)


@contextmanager
def redirect_stdout(feedback):
    """Context manager for temporarily setting a FeedbackLogger as stdout

    Parameters
    ----------
    feedback : feedback instance
        from alg decorators
    """
    oldout = sys.stdout
    sys.stdout = FeedbackLogger(feedback)
    try:
        yield
    finally:
        sys.stdout = oldout


def redirect_stdout_to_feedback(func):
    """Decorator for algorithm functions that temporarily sets a FeedbackLogger as stdout"""

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        feedback = kwargs.get("feedback", None)
        if feedback is None:
            for arg in args:
                # quacks like feedback
                if hasattr(arg, "pushConsoleInfo"):
                    feedback = arg
                    break
            else:
                raise RuntimeError(
                    "Stdout redirect requires `feedback` object as positional or keyword argument"
                )

        with redirect_stdout(feedback):
            return func(*args, **kwargs)

    return wrapped
