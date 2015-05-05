Name:           ros-hydro-rqt-pr2-dashboard
Version:        0.2.7
Release:        0%{?dist}
Summary:        ROS rqt_pr2_dashboard package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_pr2_dashboard
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-diagnostic-msgs
Requires:       ros-hydro-pr2-msgs
Requires:       ros-hydro-pr2-power-board
Requires:       ros-hydro-roslib
Requires:       ros-hydro-rospy
Requires:       ros-hydro-rqt-gui
Requires:       ros-hydro-rqt-gui-py
Requires:       ros-hydro-rqt-robot-dashboard
Requires:       ros-hydro-std-msgs
Requires:       ros-hydro-std-srvs
BuildRequires:  ros-hydro-catkin

%description
rqt_pr2_dashboard is a GUI for debugging and controlling low-level state of the
PR2. It shows things like battery status and breaker states, as well as
integrating tools like rqt_console and robot_monitor.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue May 05 2015 Devon Ash <noobaca2@gmail.com> - 0.2.7-0
- Autogenerated by Bloom

