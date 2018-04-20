# Script generated with Bloom
pkgdesc="ROS - ROS node to build a 3D map of fiducials and estimate robot pose from fiducial transforms"


pkgname='ros-kinetic-fiducial-slam'
pkgver='0.8.3_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-cv-bridge'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-fiducial-msgs'
'ros-kinetic-image-transport'
'ros-kinetic-opencv3'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf2'
'ros-kinetic-tf2-geometry-msgs'
'ros-kinetic-tf2-ros'
'ros-kinetic-visualization-msgs'
)

depends=('ros-kinetic-cv-bridge'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-fiducial-msgs'
'ros-kinetic-image-transport'
'ros-kinetic-opencv3'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf2'
'ros-kinetic-tf2-geometry-msgs'
'ros-kinetic-tf2-ros'
'ros-kinetic-visualization-msgs'
)

conflicts=()
replaces=()

_dir=fiducial_slam
source=()
md5sums=()

prepare() {
    cp -R $startdir/fiducial_slam $srcdir/fiducial_slam
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

