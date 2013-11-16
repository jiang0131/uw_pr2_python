import rospy
import actionlib
import uw_pr2_python.exceptions as ex
import pr2_controllers_msgs.msg as pr2c
import actionlib_msgs.msg as am

class Gripper(object):
    """
    Represents a gripper of the PR2
    """

    def __init__(self, side):
        """
        :param side: A string, either 'left_arm' or 'right_arm'
        """
        assert side in ['left_arm', 'right_arm']
        self._side = side
        action_name = '{0}_gripper_controller/gripper_action'.\
                      format('l' if side=='left_arm' else 'r')
        self._ac = actionlib.SimpleActionClient(action_name,
                                                pr2c.Pr2GripperCommandAction)
        rospy.loginfo("Waiting for action server {0}...".format(action_name))
        self._ac.wait_for_server()
        rospy.loginfo("Connected to action server {0}".format(action_name))

        if side == 'left_arm':
            grasp_posture_client_name = 'l_gripper_grasp_posture_controller'
        else:
            grasp_posture_client_name = 'r_gripper_grasp_posture_controller'

    def open(self, max_effort=-1):
        """
        Open this gripper
        """
        self.move(0.085, max_effort)

    def close(self, max_effort=-1):
        """
        Close this gripper
        """
        self.move(0.0, max_effort)

    def move(self, position, max_effort=-1):
        goal = pr2c.Pr2GripperCommandGoal(
            pr2c.Pr2GripperCommand(position=position, max_effort=max_effort))
        self._ac.send_goal(goal)
        rospy.loginfo("Sending goal to gripper and waiting for result...")
        self._ac.wait_for_result()
        rospy.loginfo("Gripper action returned")
        '''
        if self._ac.get_state() != am.GoalStatus.SUCCEEDED:
            raise ex.ActionFailedError()
        '''

