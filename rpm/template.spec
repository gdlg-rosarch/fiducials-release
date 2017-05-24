Name:           ros-kinetic-fiducial-pose
Version:        0.7.2
Release:        0%{?dist}
Summary:        ROS fiducial_pose package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-fiducial-msgs
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-opencv3
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-tf
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-fiducial-msgs
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-opencv3
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-tf

%description
Library to estimate 3D pose with RosbustPlanarPose

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed May 24 2017 Jim Vaughan <jimv@mrjim.com> - 0.7.2-0
- Autogenerated by Bloom

* Mon May 22 2017 Jim Vaughan <jimv@mrjim.com> - 0.7.1-0
- Autogenerated by Bloom

* Sun May 21 2017 Jim Vaughan <jimv@mrjim.com> - 0.7.0-0
- Autogenerated by Bloom

* Mon Feb 06 2017 Jim Vaughan <jimv@mrjim.com> - 0.6.1-0
- Autogenerated by Bloom

* Sat Feb 04 2017 Jim Vaughan <jimv@mrjim.com> - 0.6.0-0
- Autogenerated by Bloom

* Wed Dec 28 2016 Jim Vaughan <jimv@mrjim.com> - 0.5.1-0
- Autogenerated by Bloom

* Sat Dec 17 2016 Jim Vaughan <jimv@mrjim.com> - 0.5.0-0
- Autogenerated by Bloom

* Sun Nov 20 2016 Jim Vaughan <jimv@mrjim.com> - 0.1.2-0
- Autogenerated by Bloom

* Sat Nov 19 2016 Jim Vaughan <jimv@mrjim.com> - 0.1.1-0
- Autogenerated by Bloom

