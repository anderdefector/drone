/*
Node: Monoaranha
Subscribes to usb_cam and publishes slam_pose
Working well: 14/02/2018
*/
#include<iostream>
#include<algorithm>
#include<fstream>
#include<chrono>
#include<ros/ros.h>
#include <cv_bridge/cv_bridge.h>
#include "std_msgs/String.h"
#include<opencv2/core/core.hpp>
#include"../../../include/System.h"

using namespace std;

ros::Subscriber sub;
ros::Publisher pose_pub;

class ImageGrabber
{
public:
    ImageGrabber(ORB_SLAM2::System* pSLAM):mpSLAM(pSLAM){}

    ORB_SLAM2::System* mpSLAM;
    
    void GrabImage(const sensor_msgs::ImageConstPtr& msg)
	{
    	// Copy the ros image message to cv::Mat.
    	cv_bridge::CvImageConstPtr cv_ptr;
	    try
    	{
    	    cv_ptr = cv_bridge::toCvShare(msg);
    	}
    	catch (cv_bridge::Exception& e)
    	{
    	    ROS_ERROR("cv_bridge exception: %s", e.what());
    	    return;
    	}
    	// Pose extraction
    	cv::Mat pose = mpSLAM->TrackMonocular(cv_ptr->image,cv_ptr->header.stamp.toSec());
    	// Preparing to publish
    	std_msgs::String mens;
    	std::stringstream ss;
    
 		if(pose.empty()== true)
 		{
 			cout<<"empty"<<endl;
 		}
 		else
 		{
 			//Pose to msg
 			ss << pose.at<float>(0,0)<<","<<pose.at<float>(0,1)<<","<<pose.at<float>(0,2)<<"," <<pose.at<float>(0,3)<<","
 			   << pose.at<float>(1,0)<<","<<pose.at<float>(1,1)<<","<<pose.at<float>(1,2)<<"," <<pose.at<float>(1,3)<<","
 			   << pose.at<float>(2,0)<<","<<pose.at<float>(2,1)<<","<<pose.at<float>(2,2)<<"," <<pose.at<float>(2,3)<<","
 			   << pose.at<float>(3,0)<<","<<pose.at<float>(3,1)<<","<<pose.at<float>(3,2)<<"," <<pose.at<float>(3,3);
 			
 			//ROS publishing   
 			mens.data = ss.str();
 			pose_pub.publish(mens);
 			cout<<pose<<endl<<endl;
 		}
	}//End of function GrabImage

};//End of class ImageGrabber

int main(int argc, char **argv)
{
    ros::init(argc, argv, "MonoBebop");
    ros::start();

    if(argc != 3)
    {
        cerr << endl << "Usage: rosrun ORB_SLAM2 Monosabio path_to_vocabulary path_to_settings" << endl;        
        ros::shutdown();
        return 1;
    }    

    // Create SLAM system. It initializes all system threads and gets ready to process frames.
    ORB_SLAM2::System SLAM(argv[1],argv[2],ORB_SLAM2::System::MONOCULAR,true);

    ImageGrabber igb(&SLAM);
	
	ros::NodeHandle nodeHandler;
   	sub = nodeHandler.subscribe("bebop/image_raw", 1, &ImageGrabber::GrabImage,&igb);
   	pose_pub = nodeHandler.advertise<std_msgs::String>("slam_bebop_pose", 10);
	
    ros::spin();

    // Stop all threads
    SLAM.Shutdown();

    // Save camera trajectory
    SLAM.SaveKeyFrameTrajectoryTUM("KeyFrameTrajectory.txt");

    ros::shutdown();

    return 0;
}//End of main



