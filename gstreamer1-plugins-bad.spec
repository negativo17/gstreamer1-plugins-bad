%define _legacy_common_support 1

%global         majorminor 1.0

Name:           gstreamer1-plugins-bad
Version:        1.16.1
Release:        5%{?dist}
Epoch:          1
Summary:        GStreamer streaming media framework "bad" plugins
License:        LGPLv2+ and LGPLv2
URL:            http://gstreamer.freedesktop.org/

Source0:        http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.xz
Source1:        gstreamer-bad.appdata.xml

# Based on https://cgit.freedesktop.org/gstreamer/gst-plugins-bad/commit/?h=1.16&id=2c67d0d2f05a1dd6f3c9b6c0c7a387d738117052
Patch0:         %{name}-opencv-43.patch
# https://gitlab.freedesktop.org/gstreamer/gst-plugins-bad/-/commit/e6225482f65a12d1f2355f893b8527f24d393c23
Patch1:         %{name}-neon.patch
Patch2:         https://gitlab.freedesktop.org/gstreamer/gst-plugins-bad/-/commit/17850d7e87af93c6bd181d7c25903478c2254fa6.diff#/%{name}-vulkan.patch

# Requires Provides with and without _isa defined due to package dependencies
Obsoletes:      %{name}-free < %{?epoch}:%{version}-%{release}
Provides:       %{name}-free = %{?epoch}:%{version}-%{release}
Provides:       %{name}-free%{?_isa} = %{?epoch}:%{version}-%{release}
Obsoletes:      %{name}-free-extras < %{?epoch}:%{version}-%{release}
Provides:       %{name}-free-extras = %{?epoch}:%{version}-%{release}
Provides:       %{name}-free-extras%{?_isa} = %{?epoch}:%{version}-%{release}
Obsoletes:      %{name}-freeworld < %{?epoch}:%{version}-%{release}
Provides:       %{name}-freeworld = %{?epoch}:%{version}-%{release}
Provides:       %{name}-freeworld%{?_isa} = %{?epoch}:%{version}-%{release}
Obsoletes:      %{name}-nonfree < %{?epoch}:%{version}-%{release}
Provides:       %{name}-nonfree = %{?epoch}:%{version}-%{release}
Provides:       %{name}-nonfree%{?_isa} = %{?epoch}:%{version}-%{release}
Obsoletes:      %{name}-wildmidi < %{?epoch}:%{version}-%{release}
Provides:       %{name}-wildmidi = %{?epoch}:%{version}-%{release}
Provides:       %{name}-wildmidi%{?_isa} = %{?epoch}:%{version}-%{release}
Obsoletes:      gstreamer1-plugin-openh264 < %{?epoch}:%{version}-%{release}
Provides:       gstreamer1-plugin-openh264 = %{?epoch}:%{version}-%{release}
Provides:       gstreamer1-plugin-openh264%{?_isa} = %{?epoch}:%{version}-%{release}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  python3

BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}

BuildRequires:  bzip2-devel
BuildRequires:  check
BuildRequires:  exempi-devel
BuildRequires:  flite-devel
BuildRequires:  game-music-emu-devel
BuildRequires:  gettext-devel >= 0.17
BuildRequires:  gobject-introspection-devel >= 1.31.1
BuildRequires:  gsm-devel
BuildRequires:  gtk-doc >= 1.12
BuildRequires:  ladspa-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  orc-devel >= 0.4.17
BuildRequires:  vulkan-devel
BuildRequires:  wildmidi-devel
BuildRequires:  xvidcore-devel


BuildRequires:  pkgconfig(aom)
BuildRequires:  pkgconfig(bluez) >= 5.0
BuildRequires:  pkgconfig(cairo) >= 1.0
BuildRequires:  pkgconfig(clutter-1.0) >= 1.8
BuildRequires:  pkgconfig(clutter-glx-1.0) >= 1.8
BuildRequires:  pkgconfig(clutter-x11-1.0) >= 1.8
BuildRequires:  pkgconfig(dvdnav) >= 4.1.2
BuildRequires:  pkgconfig(dvdread) >= 4.1.2
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fdk-aac) >= 0.1.4
BuildRequires:  pkgconfig(fluidsynth) >= 1.0
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0) > 2.24
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gstreamer-allocators-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.15
BuildRequires:  pkgconfig(gtk+-wayland-3.0)
BuildRequires:  pkgconfig(gtk+-x11-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(kate) >= 0.1.7
BuildRequires:  pkgconfig(lcms2) >= 2.7
BuildRequires:  pkgconfig(libass) >= 0.10.2
BuildRequires:  pkgconfig(libbs2b) >= 3.1.0
BuildRequires:  pkgconfig(libchromaprint)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcurl) >= 7.35.0
BuildRequires:  pkgconfig(libdca)
BuildRequires:  pkgconfig(libdc1394-2) >= 2.0.0
BuildRequires:  pkgconfig(libde265) >= 0.9
BuildRequires:  pkgconfig(libdrm) >= 2.4.55
BuildRequires:  pkgconfig(libexif) >= 0.6.16
BuildRequires:  pkgconfig(libmms) >= 0.4
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libofa) >= 0.9.3
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libopenmpt)
BuildRequires:  pkgconfig(libpng) >= 1.0
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.36.2
BuildRequires:  pkgconfig(librtmp)
BuildRequires:  pkgconfig(libSoundTouch)
BuildRequires:  pkgconfig(libsrtp)
BuildRequires:  pkgconfig(libssh2) >= 1.4.3
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libvisual-0.4) >= 0.4.0
BuildRequires:  pkgconfig(libwebp) >= 0.2.1
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.2
BuildRequires:  pkgconfig(mjpegtools) >= 2.0.0
BuildRequires:  pkgconfig(neon) >= 0.27.0
BuildRequires:  pkgconfig(neon) <= 0.31.99
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(nice) >= 0.1.14
BuildRequires:  pkgconfig(openal) >= 1.14
BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(openh264) >= 1.3.0
BuildRequires:  pkgconfig(openssl) >= 1.0.1
BuildRequires:  pkgconfig(opus) >= 0.9.4
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5WaylandClient)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(sbc) >= 1.0
BuildRequires:  pkgconfig(schroedinger-1.0) >= 1.0.10
BuildRequires:  pkgconfig(sndfile) >= 1.0.16
BuildRequires:  pkgconfig(soundtouch) >= 1.4
BuildRequires:  pkgconfig(spandsp) >= 0.0.6
BuildRequires:  pkgconfig(tiger) >= 0.3.2
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(vo-aacenc) >= 0.1.0
BuildRequires:  pkgconfig(vo-amrwbenc) >= 0.1.0
BuildRequires:  pkgconfig(wayland-client) >= 1.4.0
BuildRequires:  pkgconfig(wayland-cursor) >= 1.0
BuildRequires:  pkgconfig(wayland-egl) >= 9.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.4
BuildRequires:  pkgconfig(webrtc-audio-processing) >= 0.2
BuildRequires:  pkgconfig(webrtc-audio-processing) < 0.4
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x265)
BuildRequires:  pkgconfig(xcb) >= 1.10
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(zbar) >= 0.9
BuildRequires:  pkgconfig(zvbi-0.2)

%ifarch x86_64
# Nvidia encoder/decoder + Intel QuickSync plugin build requirements
BuildRequires:  pkgconfig(cuda)
BuildRequires:  pkgconfig(cudart)
BuildRequires:  pkgconfig(libmfx)
BuildRequires:  nvenc >= 1:8.2.16
%endif

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that aren't tested well enough, or the code is
not of good enough quality.

%package        fluidsynth
Summary:        GStreamer "bad" fluidsynth plugin
Requires:       %{name}%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       soundfont2-default
Obsoletes:      %{name}-free-fluidsynth < %{?epoch}:%{version}-%{release}
Provides:       %{name}-free-fluidsynth = %{?epoch}:%{version}-%{release}
Provides:       %{name}-free-fluidsynth%{?_isa} = %{?epoch}:%{version}-%{release}

%description    fluidsynth
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that aren't tested well enough, or the code is
not of good enough quality.

This package contains the fluidsynth plugin

%ifarch x86_64
%package        nvidia
Summary:        GStreamer "bad" nvdec/nvenc plugins
Requires:       %{name}%{?_isa} = %{?epoch}:%{version}-%{release}
Obsoletes:      %{name}-nvenc < %{?epoch}:%{version}-%{release}
Provides:       %{name}-nvenc = %{?epoch}:%{version}-%{release}
Provides:       %{name}-nvenc%{?_isa} = %{?epoch}:%{version}-%{release}

%description    nvidia
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that aren't tested well enough, or the code is
not of good enough quality.

This package contains the Nvidia NVENCODE/NVDECODE(CUVID) plugins.
%endif

%package        devel
Summary:        Development files for the GStreamer media framework "bad" plug-ins
Requires:       %{name}%{?_isa} = %{?epoch}:%{version}-%{release}
Requires:       gstreamer1-plugins-base-devel
Obsoletes:      %{name}-free-devel < %{?epoch}:%{version}-%{release}
Provides:       %{name}-free-devel = %{?epoch}:%{version}-%{release}
Provides:       %{name}-free-devel%{?_isa} = %{?epoch}:%{version}-%{release}

%description    devel
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains the development files for the plug-ins that aren't tested
well enough, or the code is not of good enough quality.

%prep
%autosetup -p1 -n gst-plugins-bad-%{version}

%build
autoreconf -vif

%ifarch x86_64
export CUDA_CFLAGS="-I%{_includedir}/cuda -I%{_includedir}/nvenc"
export CUDA_LIBS="-L%{_libdir} -lcuda -lcudart"
export NVENCODE_CFLAGS="-I%{_includedir}/nvenc"
export MSDK_CFLAGS="$MSDK_CFLAGS -I%{_includedir}/mfx"
%endif

%configure \
    --disable-rpath \
    --disable-silent-rules \
    --disable-fatal-warnings \
    --disable-faac \
    --disable-faad \
    --enable-android_media \
    --enable-aom \
    --enable-apple_media \
    --enable-assrender \
    --enable-avc \
    --enable-bluez \
    --enable-bs2b \
    --enable-bz2 \
    --enable-chromaprint \
    --enable-curl \
    --enable-dash \
    --enable-dc1394 \
    --enable-decklink \
    --enable-directfb \
    --enable-dtls \
    --enable-dts \
    --enable-dvb \
    --enable-experimental \
    --enable-fbdev \
    --enable-fdk_aac \
    --enable-flite \
    --enable-fluidsynth \
    --enable-gl \
    --enable-gme \
    --enable-gsm \
    --enable-gtk-doc \
    --enable-hls \
    --enable-ipcpipeline \
    --enable-kate \
    --enable-kms \
    --enable-ladspa \
    --enable-lcms2 \
    --enable-libde265 \
    --enable-libmms \
    --enable-modplug \
    --enable-mpeg2enc \
    --enable-mplex \
    --enable-musepack \
    --enable-neon \
    --enable-ofa \
    --enable-openal \
    --enable-opencv \
    --enable-openexr \
    --enable-openh264 \
    --enable-openjpeg \
    --enable-openmpt \
    --enable-openni2 \
    --enable-opensles \
    --enable-opus \
    --enable-resindvd \
    --enable-rsvg \
    --enable-rtmp \
    --enable-sbc \
    --enable-shm \
    --enable-smoothstreaming \
    --enable-sndfile \
    --enable-soundtouch \
    --enable-spandsp \
    --enable-srt \
    --enable-srtp \
    --enable-teletextdec \
    --enable-tinyalsa \
    --enable-ttml \
    --enable-uvch264 \
    --enable-vdpau \
    --enable-voaacenc \
    --enable-voamrwbenc \
    --enable-vulkan \
    --enable-wasapi \
    --enable-wayland \
    --enable-webp \
    --enable-webrtc \
    --enable-webrtcdsp \
    --enable-wildmidi \
    --enable-winks \
    --enable-x265 \
    --enable-zbar \
    --with-package-name="Fedora GStreamer-plugins-bad package" \
    --with-package-origin="https://negativo17.org" \
%ifarch x86_64
    --enable-cuda \
    --enable-msdk \
    --enable-nvdec \
    --enable-nvenc \
    --with-cuda-prefix=%{_prefix} \
    --with-msdk-prefix=%{_prefix} \
%endif

%make_build

%install
%make_install
install -p -m 644 -D %{SOURCE1} %{buildroot}%{_metainfodir}/gstreamer-bad.metainfo.xml
find %{buildroot} -name '*.la' -delete
%find_lang gst-plugins-bad-%{majorminor}

%files -f gst-plugins-bad-%{majorminor}.lang
%license COPYING COPYING.LIB
%doc AUTHORS README REQUIREMENTS
%{_metainfodir}/gstreamer-bad.metainfo.xml
%{_libdir}/girepository-%{majorminor}/GstInsertBin-%{majorminor}.typelib
%{_libdir}/girepository-%{majorminor}/GstMpegts-%{majorminor}.typelib
%{_libdir}/girepository-%{majorminor}/GstPlayer-%{majorminor}.typelib
%{_libdir}/girepository-%{majorminor}/GstWebRTC-%{majorminor}.typelib
%{_libdir}/libgstadaptivedemux-%{majorminor}.so.*
%{_libdir}/libgstbadaudio-%{majorminor}.so.*
%{_libdir}/libgstbasecamerabinsrc-%{majorminor}.so.*
%{_libdir}/libgstcodecparsers-%{majorminor}.so.*
%{_libdir}/libgstinsertbin-%{majorminor}.so.*
%{_libdir}/libgstisoff-%{majorminor}.so.*
%{_libdir}/libgstmpegts-%{majorminor}.so.*
%{_libdir}/libgstopencv-%{majorminor}.so.*
%{_libdir}/libgstphotography-%{majorminor}.so.*
%{_libdir}/libgstplayer-%{majorminor}.so.*
%{_libdir}/libgstsctp-%{majorminor}.so.*
%{_libdir}/libgsturidownloader-%{majorminor}.so.*
%{_libdir}/libgstwayland-%{majorminor}.so.*
%{_libdir}/libgstwebrtc-%{majorminor}.so.*
# Presets
%dir %{_datadir}/gstreamer-%{majorminor}/presets/
%{_datadir}/gstreamer-%{majorminor}/presets/GstFreeverb.prs
%{_datadir}/gstreamer-%{majorminor}/presets/GstVoAmrwbEnc.prs
# OpenCV data
%dir %{_datadir}/gst-plugins-bad/%{majorminor}/opencv_haarcascades/
%{_datadir}/gst-plugins-bad/%{majorminor}/opencv_haarcascades/fist.xml
%{_datadir}/gst-plugins-bad/%{majorminor}/opencv_haarcascades/palm.xml
# Plugins
%{_libdir}/gstreamer-%{majorminor}/libgstaccurip.so
%{_libdir}/gstreamer-%{majorminor}/libgstadpcmdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstadpcmenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstaiff.so
%{_libdir}/gstreamer-%{majorminor}/libgstaom.so
%{_libdir}/gstreamer-%{majorminor}/libgstasfmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstassrender.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiobuffersplit.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiofxbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiolatency.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiomixmatrix.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiovisualizers.so
%{_libdir}/gstreamer-%{majorminor}/libgstautoconvert.so
%{_libdir}/gstreamer-%{majorminor}/libgstbayer.so
%{_libdir}/gstreamer-%{majorminor}/libgstbluez.so
%{_libdir}/gstreamer-%{majorminor}/libgstbs2b.so
%{_libdir}/gstreamer-%{majorminor}/libgstbz2.so
%{_libdir}/gstreamer-%{majorminor}/libgstclosedcaption.so
%{_libdir}/gstreamer-%{majorminor}/libgstcamerabin.so
%{_libdir}/gstreamer-%{majorminor}/libgstchromaprint.so
%{_libdir}/gstreamer-%{majorminor}/libgstcoloreffects.so
%{_libdir}/gstreamer-%{majorminor}/libgstcolormanagement.so
%{_libdir}/gstreamer-%{majorminor}/libgstcurl.so
%{_libdir}/gstreamer-%{majorminor}/libgstdashdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstdc1394.so
%{_libdir}/gstreamer-%{majorminor}/libgstde265.so
%{_libdir}/gstreamer-%{majorminor}/libgstdebugutilsbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstdecklink.so
%{_libdir}/gstreamer-%{majorminor}/libgstdtls.so
%{_libdir}/gstreamer-%{majorminor}/libgstdtsdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvb.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvbsuboverlay.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdspu.so
%{_libdir}/gstreamer-%{majorminor}/libgstfaceoverlay.so
%{_libdir}/gstreamer-%{majorminor}/libgstfbdevsink.so
%{_libdir}/gstreamer-%{majorminor}/libgstfdkaac.so
%{_libdir}/gstreamer-%{majorminor}/libgstfestival.so
%{_libdir}/gstreamer-%{majorminor}/libgstfieldanalysis.so
%{_libdir}/gstreamer-%{majorminor}/libgstflite.so
%{_libdir}/gstreamer-%{majorminor}/libgstfreeverb.so
%{_libdir}/gstreamer-%{majorminor}/libgstfrei0r.so
%{_libdir}/gstreamer-%{majorminor}/libgstgaudieffects.so
%{_libdir}/gstreamer-%{majorminor}/libgstgdp.so
%{_libdir}/gstreamer-%{majorminor}/libgstgeometrictransform.so
%{_libdir}/gstreamer-%{majorminor}/libgstgme.so
%{_libdir}/gstreamer-%{majorminor}/libgstgsm.so
%{_libdir}/gstreamer-%{majorminor}/libgsthls.so
%{_libdir}/gstreamer-%{majorminor}/libgstid3tag.so
%{_libdir}/gstreamer-%{majorminor}/libgstinterlace.so
%{_libdir}/gstreamer-%{majorminor}/libgstinter.so
%{_libdir}/gstreamer-%{majorminor}/libgstivfparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstivtc.so
%{_libdir}/gstreamer-%{majorminor}/libgstjp2kdecimator.so
%{_libdir}/gstreamer-%{majorminor}/libgstjpegformat.so
%{_libdir}/gstreamer-%{majorminor}/libgstkate.so
%{_libdir}/gstreamer-%{majorminor}/libgstkms.so
%{_libdir}/gstreamer-%{majorminor}/libgstladspa.so
%{_libdir}/gstreamer-%{majorminor}/libgstlegacyrawparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstmms.so
%{_libdir}/gstreamer-%{majorminor}/libgstmodplug.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2enc.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegpsdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegpsmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmplex.so
%ifarch x86_64
%{_libdir}/gstreamer-%{majorminor}/libgstmsdk.so
%endif
%{_libdir}/gstreamer-%{majorminor}/libgstmxf.so
%{_libdir}/gstreamer-%{majorminor}/libgstneonhttpsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstnetsim.so
%{_libdir}/gstreamer-%{majorminor}/libgstofa.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenal.so
%{_libdir}/gstreamer-%{majorminor}/libgstopencv.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenexr.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenh264.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenjpeg.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenmpt.so
%{_libdir}/gstreamer-%{majorminor}/libgstopusparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstpcapparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstipcpipeline.so
%{_libdir}/gstreamer-%{majorminor}/libgstpnm.so
%{_libdir}/gstreamer-%{majorminor}/libgstproxy.so
%{_libdir}/gstreamer-%{majorminor}/libgstremovesilence.so
%{_libdir}/gstreamer-%{majorminor}/libgstresindvd.so
%{_libdir}/gstreamer-%{majorminor}/libgstrfbsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstrsvg.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtmp.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtponvif.so
%{_libdir}/gstreamer-%{majorminor}/libgstsbc.so
%{_libdir}/gstreamer-%{majorminor}/libgstsdpelem.so
%{_libdir}/gstreamer-%{majorminor}/libgstsegmentclip.so
%{_libdir}/gstreamer-%{majorminor}/libgstshm.so
%{_libdir}/gstreamer-%{majorminor}/libgstsiren.so
%{_libdir}/gstreamer-%{majorminor}/libgstsmooth.so
%{_libdir}/gstreamer-%{majorminor}/libgstsmoothstreaming.so
%{_libdir}/gstreamer-%{majorminor}/libgstsndfile.so
%{_libdir}/gstreamer-%{majorminor}/libgstsoundtouch.so
%{_libdir}/gstreamer-%{majorminor}/libgstspandsp.so
%{_libdir}/gstreamer-%{majorminor}/libgstspeed.so
%{_libdir}/gstreamer-%{majorminor}/libgstsrtp.so
%{_libdir}/gstreamer-%{majorminor}/libgstsubenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstteletext.so
%{_libdir}/gstreamer-%{majorminor}/libgsttimecode.so
%{_libdir}/gstreamer-%{majorminor}/libgstttmlsubs.so
%{_libdir}/gstreamer-%{majorminor}/libgstuvch264.so
%{_libdir}/gstreamer-%{majorminor}/libgstvdpau.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideofiltersbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideoframe_audiolevel.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideoparsersbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideosignal.so
%{_libdir}/gstreamer-%{majorminor}/libgstvmnc.so
%{_libdir}/gstreamer-%{majorminor}/libgstvoaacenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstvoamrwbenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstvulkan.so
%{_libdir}/gstreamer-%{majorminor}/libgstwebp.so
%{_libdir}/gstreamer-%{majorminor}/libgstwebrtc.so
%{_libdir}/gstreamer-%{majorminor}/libgstwebrtcdsp.so
%{_libdir}/gstreamer-%{majorminor}/libgstx265.so
%{_libdir}/gstreamer-%{majorminor}/libgsty4mdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstyadif.so
%{_libdir}/gstreamer-%{majorminor}/libgstzbar.so
%{_libdir}/gstreamer-%{majorminor}/libgstwaylandsink.so

%files fluidsynth
%{_libdir}/gstreamer-%{majorminor}/libgstfluidsynthmidi.so
%{_libdir}/gstreamer-%{majorminor}/libgstmidi.so
%{_libdir}/gstreamer-%{majorminor}/libgstwildmidi.so

%ifarch x86_64
%files nvidia
%{_libdir}/gstreamer-%{majorminor}/libgstnvdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstnvenc.so
%endif

%files devel
%doc %{_datadir}/gtk-doc/html/*
%{_datadir}/gir-%{majorminor}/GstInsertBin-%{majorminor}.gir
%{_datadir}/gir-%{majorminor}/GstMpegts-%{majorminor}.gir
%{_datadir}/gir-%{majorminor}/GstPlayer-%{majorminor}.gir
%{_datadir}/gir-%{majorminor}/GstWebRTC-%{majorminor}.gir
%{_includedir}/gstreamer-%{majorminor}/gst/*
%{_libdir}/lib*-%{majorminor}.so
%{_libdir}/pkgconfig/gstreamer-*-%{majorminor}.pc

%changelog
* Wed Feb 08 2023 Simone Caronni <negativo17@gmail.com> - 1:1.16.1-5
- SPEC file cleanup.

* Tue Feb 07 2023 Simone Caronni <negativo17@gmail.com> - 1:1.16.1-4
- First build for el8.
- Disable FAAC Encoder/Decoder as it creates more problems than anything.
- Update SPEC file.
- Remove obsolete build options.

* Thu Dec 19 2019 Simone Caronni <negativo17@gmail.com> - 1:1.16.1-3
- Add missing BR.

* Mon Oct 21 2019 Simone Caronni <negativo17@gmail.com> - 1:1.16.1-2
- Rebuild for updated dependencies.

* Mon Oct 07 2019 Simone Caronni <negativo17@gmail.com> - 1:1.16.1-1
- Update to 1.16.1.

* Sun Jul 07 2019 Simone Caronni <negativo17@gmail.com> - 1:1.16.0-2
- Rebuild for updated dependencies.

* Tue Apr 30 2019 Simone Caronni <negativo17@gmail.com> - 1:1.16.0-1
- Update to 1.16.0.
- Disable webkit backend.

* Thu Apr 04 2019 Simone Caronni <negativo17@gmail.com> - 1:1.15.2-2
- Enable additional plugins.
- Trim changelog.

* Wed Apr 03 2019 Simone Caronni <negativo17@gmail.com> - 1:1.15.2-1
- Update to 1.15.2.

* Thu Jan 03 2019 Simone Caronni <negativo17@gmail.com> - 1:1.14.4-3
- Backport support for CUDA 10.0.
- Backport switch to Video Codec SDK headers for nvenc/nvdec plugins. This links
  the libraries, so split out the plugins into its own subpackage.

* Thu Nov 15 2018 Simone Caronni <negativo17@gmail.com> - 1:1.14.4-2
- Rebuild for updated x265.

* Sat Oct 20 2018 Simone Caronni <negativo17@gmail.com> - 1:1.14.4-1
- Update to 1.14.4.

* Wed Sep 26 2018 Simone Caronni <negativo17@gmail.com> - 1:1.14.3-1
- Update to 1.14.3.

* Tue Aug 28 2018 Simone Caronni <negativo17@gmail.com> - 1:1.14.2-1
- Update to 1.14.2.
- Add support for CUDA 9.2.

* Mon Jul 16 2018 Simone Caronni <negativo17@gmail.com> - 1:1.14.1-4
- Rebuild for updated dependencies.

* Wed Jul 04 2018 Simone Caronni <negativo17@gmail.com> - 1:1.14.1-3
- Update CUDA/NVENC plugin build.

* Fri Jun 29 2018 Simone Caronni <negativo17@gmail.com> - 1:1.14.1-2
- Rebuild for udpated dependencies.

* Thu Jun 14 2018 Simone Caronni <negativo17@gmail.com> - 1:1.14.1-1
- Update to 1.14.1.

* Wed May 02 2018 Simone Caronni <negativo17@gmail.com> - 1:1.14.0-1
- Update to 1.14.0.
- Update SPEC file.

* Thu Jan 18 2018 Simone Caronni <negativo17@gmail.com> - 1:1.12.4-2
- Require OpenJpeg 2.

* Tue Jan 09 2018 Simone Caronni <negativo17@gmail.com> - 1:1.12.4-1
- Update to 1.12.4.

* Wed Oct 25 2017 Simone Caronni <negativo17@gmail.com> - 1:1.12.3-2
- Rebuild for x265 and OpenH264 updates.

* Mon Oct 23 2017 Simone Caronni <negativo17@gmail.com> - 1:1.12.3-1
- Update to 1.12.3.

* Wed Aug 23 2017 Simone Caronni <negativo17@gmail.com> - 1:1.12.2-2
- Rebuild for x265 update.

* Thu Jul 20 2017 Simone Caronni <negativo17@gmail.com> - 1:1.12.2-1
- Update to 1.12.2.

* Tue Jun 27 2017 Simone Caronni <negativo17@gmail.com> - 1:1.12.1-2
- Fix typos in Obsoletes/Provides.

* Sat Jun 24 2017 Simone Caronni <negativo17@gmail.com> - 1:1.12.1-1
- Update to 1.12.1.

* Sat May 13 2017 Simone Caronni <negativo17@gmail.com> - 1:1.12.0-1
- Update to 1.12.0.

* Thu Apr 20 2017 Simone Caronni <negativo17@gmail.com> - 1:1.11.90-3
- Enable NVENC plugin with CUDA 8 patches.

* Wed Apr 19 2017 Simone Caronni <negativo17@gmail.com> - 1:1.11.90-2
- Gtk plugin is free-gtk and not bad-gtk.

* Wed Apr 19 2017 Simone Caronni <negativo17@gmail.com> - 1:1.11.90-1
- Update to 1.11.90.

* Thu Mar 30 2017 Simone Caronni <negativo17@gmail.com> - 1:1.11.2-1
- Update to 1.11.2.
- Enable fdk-aac, lv2, vulkan plugins.
- Integrate nvenc in main package.
- Momentarily disable mms, mimic, nvenc plugins.

* Tue Mar 07 2017 Simo Sorce <simo@ssimo.org> - 1:1.10.4-2
- Rebuild with webrtc-echo support

* Mon Feb 27 2017 Simone Caronni <negativo17@gmail.com> - 1:1.10.4-1
- Update to 1.10.4.

* Tue Jan 31 2017 Simone Caronni <negativo17@gmail.com> - 1:1.10.3-1
- Update to 1.10.3.

* Tue Jan 03 2017 Simone Caronni <negativo17@gmail.com> - 1:1.10.2-2
- Rebuild for x265 2.2 update.
