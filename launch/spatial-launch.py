# Copyright 2019 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Launch a Phidgets spatial in a component container."""

import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode


def generate_launch_description():
    """Generate launch description with multiple components."""
    container = ComposableNodeContainer(
            name='phidget_container',
            namespace='',
            package='rclcpp_components',
            executable='component_container',
            composable_node_descriptions=[
                ComposableNode(
                    package='phidgets_spatial',
                    plugin='phidgets::SpatialRosI',
                    name='phidgets_530779',
                    parameters=[{
                        'serial':530779,
                        'raw_topic_name':'imu_530779/data_raw',
                        'cal_topic_name':'imu_530779/is_calibrated',
                        'cal_service_name':'imu_530779/calibrate',
                        'mag_topic_name':'imu_530779/mag'
                    }]
                    ),
                ComposableNode(
                    package='phidgets_spatial',
                    plugin='phidgets::SpatialRosI',
                    name='phidgets_530809',
                    parameters=[{
                        'serial':530809,
                        'raw_topic_name':'imu_530809/data_raw',
                        'cal_topic_name':'imu_530809/is_calibrated',
                        'cal_service_name':'imu_530809/calibrate',
                        'mag_topic_name':'imu_530809/mag'
                    }]
                    
                    ),
                 ComposableNode(
                    package='phidgets_spatial',
                    plugin='phidgets::SpatialRosI',
                    name='phidgets_531450',
                    parameters=[{
                        'serial':531450,
                        'raw_topic_name':'imu_531450/data_raw',
                        'cal_topic_name':'imu_531450/is_calibrated',
                        'cal_service_name':'imu_531450/calibrate',
                        'mag_topic_name':'imu_531450/mag'
                    }]
                    )
            ],
            output='both',
    )

    return launch.LaunchDescription([container])
