Name:           ros-kinetic-fiducial-msgs
Version:        0.8.0
Release:        0%{?dist}
Summary:        ROS fiducial_msgs package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-tf
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-tf

%description
Package containing message definitions for fiducials

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
* Sun Jan 14 2018 Jim Vaughan <jimv@mrjim.com> - 0.8.0-0
- Autogenerated by Bloom

* Wed Dec 06 2017 Jim Vaughan <jimv@mrjim.com> - 0.7.5-0
- Autogenerated by Bloom

* Thu Nov 09 2017 Jim Vaughan <jimv@mrjim.com> - 0.7.4-0
- Autogenerated by Bloom

* Sun Jul 16 2017 Jim Vaughan <jimv@mrjim.com> - 0.7.3-0
- Autogenerated by Bloom

* Wed May 24 2017 Jim Vaughan <jimv@mrjim.com> - 0.7.2-0
- Autogenerated by Bloom

* Mon May 22 2017 Jim Vaughan <jimv@mrjim.com> - 0.7.1-0
- Autogenerated by Bloom

* Sun May 21 2017 Jim Vaughan <jimv@mrjim.com> - 0.7.0-0
- Autogenerated by Bloom

