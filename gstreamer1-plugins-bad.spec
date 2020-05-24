%ifarch x86_64
%global         _with_cuda 1
%endif

%global         majorminor 1.0

Name:           gstreamer1-plugins-bad
Version:        1.14.4
Release:        5%{?dist}
Epoch:          1
Summary:        GStreamer streaming media framework "bad" plugins
License:        LGPLv2+ and LGPLv2
URL:            http://gstreamer.freedesktop.org/

Source0:        http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.xz

Patch0:         %{name}-cuda.patch
Patch1:         %{name}-fdk-aac-v2.patch
Patch2:         %{name}-openh264-v2.patch

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
#BuildRequires:  jasper-devel
BuildRequires:  ladspa-devel
BuildRequires:  libcdaudio-devel
BuildRequires:  libiptcdata-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  orc-devel >= 0.4.17
#BuildRequires:  spc-devel
BuildRequires:  vulkan-devel
BuildRequires:  wildmidi-devel
BuildRequires:  xvidcore-devel

BuildRequires:  pkgconfig(aom)
BuildRequires:  pkgconfig(bluez) >= 5.0
BuildRequires:  pkgconfig(cairo) >= 1.0
BuildRequires:  pkgconfig(clutter-1.0) >= 1.8
BuildRequires:  pkgconfig(clutter-glx-1.0) >= 1.8
BuildRequires:  pkgconfig(clutter-x11-1.0) >= 1.8
#BuildRequires:  pkgconfig(daaladec)
#BuildRequires:  pkgconfig(daalaenc)
#BuildRequires:  pkgconfig(dssim)
BuildRequires:  pkgconfig(dvdnav) >= 4.1.2
BuildRequires:  pkgconfig(dvdread) >= 4.1.2
BuildRequires:  pkgconfig(fdk-aac) >= 0.1.4
BuildRequires:  pkgconfig(fluidsynth) >= 1.0
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0) > 2.24
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
#BuildRequires:  pkgconfig(gnustl)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.15
BuildRequires:  pkgconfig(gtk+-wayland-3.0)
BuildRequires:  pkgconfig(gtk+-x11-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(kate) >= 0.1.7
#BuildRequires:  pkgconfig(lcms2) >= 2.7
BuildRequires:  pkgconfig(libass) >= 0.10.2
BuildRequires:  pkgconfig(libbs2b) >= 3.1.0
BuildRequires:  pkgconfig(libchromaprint)
BuildRequires:  pkgconfig(libcrypto)
#BuildRequires:  pkgconfig(libcurl) >= 7.35.0
BuildRequires:  pkgconfig(libdc1394-2) >= 2.0.0
BuildRequires:  pkgconfig(libde265) >= 0.9
BuildRequires:  pkgconfig(libdrm) >= 2.4.55
BuildRequires:  pkgconfig(libexif) >= 0.6.16
BuildRequires:  pkgconfig(libmfx)
BuildRequires:  pkgconfig(libmms) >= 0.4
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libofa) >= 0.9.3
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libopenmpt)
#BuildRequires:  pkgconfig(libopenni2) >= 0.26
BuildRequires:  pkgconfig(libpng) >= 1.0
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.36.2
BuildRequires:  pkgconfig(librtmp)
BuildRequires:  pkgconfig(libSoundTouch)
BuildRequires:  pkgconfig(libsrtp)
#BuildRequires:  pkgconfig(libsrtp2) >= 2.1.0
BuildRequires:  pkgconfig(libssh2) >= 1.4.3
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libvisual-0.4) >= 0.4.0
BuildRequires:  pkgconfig(libwebp) >= 0.2.1
#BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.2
#BuildRequires:  pkgconfig(lilv-0) >= 0.22
BuildRequires:  pkgconfig(lrdf)
BuildRequires:  pkgconfig(mjpegtools) >= 2.0.0
BuildRequires:  pkgconfig(neon) >= 0.27.0
BuildRequires:  pkgconfig(neon) <= 0.30.99
BuildRequires:  pkgconfig(nettle)
#BuildRequires:  pkgconfig(nice) >= 0.1.14
BuildRequires:  pkgconfig(openal) >= 1.14
BuildRequires:  pkgconfig(opencv) >= 2.3.0
BuildRequires:  pkgconfig(opencv) <= 3.5.0
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
BuildRequires:  pkgconfig(slv2) >= 0.6.6
BuildRequires:  pkgconfig(sndfile) >= 1.0.16
#BuildRequires:  pkgconfig(soundtouch) >= 1.4
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
BuildRequires:  pkgconfig(zbar) >= 0.9
BuildRequires:  pkgconfig(zvbi-0.2)

%{?_with_cuda:
# Nvidia encoder/decoder (nvenc/nvdec) plugin build requirements
BuildRequires:  pkgconfig(cuda)
BuildRequires:  pkgconfig(cudart)
BuildRequires:  nvenc >= 1:8.2.16
}

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

%{?_with_cuda:
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
}

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

sed -i -e 's/-Wno-portability 1.14/-Wno-portability/g' configure.ac

%build
autoreconf -vif
export CUDA_CFLAGS="-I%{_includedir}/cuda -I%{_includedir}/nvenc"
export CUDA_LIBS="-L%{_libdir} -lcuda -lcudart"
export NVENCODE_CFLAGS="-I%{_includedir}/nvenc"
export MSDK_CFLAGS="$MSDK_CFLAGS -I%{_includedir}/mfx"
%configure \
    --disable-rpath \
    --disable-silent-rules \
    --disable-fatal-warnings \
    --disable-faac \
    --disable-faad \
    --enable-acm \
    --enable-android_media \
    --enable-aom \
    --enable-apple_media \
    --enable-assrender \
    --enable-avc \
    --enable-bluez \
    --enable-bs2b \
    --enable-bz2 \
    --enable-chromaprint \
    --enable-cuda \
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
    --enable-lv2 \
    --enable-modplug \
    --enable-mpeg2enc \
    --enable-mplex \
    --enable-msdk \
    --enable-musepack \
    --enable-neon \
    --enable-nvdec \
    --enable-nvenc \
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
    --enable-spc \
    --enable-srt \
    --enable-srtp \
    --enable-teletextdec \
    --enable-tinyalsa \
    --enable-ttml \
    --enable-uvch264 \
    --enable-vcd \
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
    --with-cuda-prefix=%{_prefix} \
    --with-msdk-prefix=%{_prefix} \
    --with-package-name="Fedora GStreamer-plugins-bad package" \
    --with-package-origin="http://negativo17.org"

%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete
%find_lang gst-plugins-bad-%{majorminor}

%ldconfig_scriptlets

%files -f gst-plugins-bad-%{majorminor}.lang
%license COPYING COPYING.LIB
%doc AUTHORS README REQUIREMENTS
%dir %{_datadir}/gstreamer-%{majorminor}/presets/
%{_datadir}/gstreamer-%{majorminor}/presets/GstFreeverb.prs
%{_datadir}/gstreamer-%{majorminor}/presets/GstVoAmrwbEnc.prs
%dir %{_datadir}/gst-plugins-bad/%{majorminor}/opencv_haarcascades/
%{_datadir}/gst-plugins-bad/%{majorminor}/opencv_haarcascades/fist.xml
%{_datadir}/gst-plugins-bad/%{majorminor}/opencv_haarcascades/palm.xml
%{_libdir}/girepository-%{majorminor}/GstInsertBin-%{majorminor}.typelib
%{_libdir}/girepository-%{majorminor}/GstMpegts-%{majorminor}.typelib
%{_libdir}/girepository-%{majorminor}/GstPlayer-%{majorminor}.typelib
%{_libdir}/girepository-%{majorminor}/GstWebRTC-%{majorminor}.typelib
%{_libdir}/libgstadaptivedemux-%{majorminor}.so.*
%{_libdir}/libgstbadaudio-%{majorminor}.so.*
%{_libdir}/libgstbadvideo-%{majorminor}.so.*
%{_libdir}/libgstbasecamerabinsrc-%{majorminor}.so.*
%{_libdir}/libgstcodecparsers-%{majorminor}.so.*
%{_libdir}/libgstinsertbin-%{majorminor}.so.*
%{_libdir}/libgstisoff-%{majorminor}.so.*
%{_libdir}/libgstmpegts-%{majorminor}.so.*
%{_libdir}/libgstopencv-%{majorminor}.so.*
%{_libdir}/libgstphotography-%{majorminor}.so.*
%{_libdir}/libgstplayer-%{majorminor}.so.*
%{_libdir}/libgsturidownloader-%{majorminor}.so.*
%{_libdir}/libgstwayland-%{majorminor}.so.*
%{_libdir}/libgstwebrtc-%{majorminor}.so.*
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
%{_libdir}/gstreamer-%{majorminor}/libgstcamerabin.so
%{_libdir}/gstreamer-%{majorminor}/libgstchromaprint.so
%{_libdir}/gstreamer-%{majorminor}/libgstcoloreffects.so
#%{_libdir}/gstreamer-%{majorminor}/libgstcolormanagement.so
%{_libdir}/gstreamer-%{majorminor}/libgstcompositor.so
#%{_libdir}/gstreamer-%{majorminor}/libgstcurl.so
%{_libdir}/gstreamer-%{majorminor}/libgstdashdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstdc1394.so
%{_libdir}/gstreamer-%{majorminor}/libgstde265.so
%{_libdir}/gstreamer-%{majorminor}/libgstdebugutilsbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstdecklink.so
%{_libdir}/gstreamer-%{majorminor}/libgstdtls.so
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
#%{_libdir}/gstreamer-%{majorminor}/libgstlv2.so
%{_libdir}/gstreamer-%{majorminor}/libgstmms.so
%{_libdir}/gstreamer-%{majorminor}/libgstmodplug.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2enc.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegpsdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegpsmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmplex.so
%{_libdir}/gstreamer-%{majorminor}/libgstmsdk.so
%{_libdir}/gstreamer-%{majorminor}/libgstmusepack.so
%{_libdir}/gstreamer-%{majorminor}/libgstmxf.so
%{_libdir}/gstreamer-%{majorminor}/libgstneonhttpsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstnetsim.so
%{_libdir}/gstreamer-%{majorminor}/libgstofa.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenal.so
%{_libdir}/gstreamer-%{majorminor}/libgstopencv.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenexr.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenglmixers.so
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
%{_libdir}/gstreamer-%{majorminor}/libgststereo.so
%{_libdir}/gstreamer-%{majorminor}/libgstsubenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstteletext.so
%{_libdir}/gstreamer-%{majorminor}/libgsttimecode.so
#%{_libdir}/gstreamer-%{majorminor}/libgstttmlsubs.so
%{_libdir}/gstreamer-%{majorminor}/libgstuvch264.so
%{_libdir}/gstreamer-%{majorminor}/libgstvcdsrc.so
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
#%{_libdir}/gstreamer-%{majorminor}/libgstwebrtc.so
%{_libdir}/gstreamer-%{majorminor}/libgstwebrtcdsp.so
%{_libdir}/gstreamer-%{majorminor}/libgstx265.so
%{_libdir}/gstreamer-%{majorminor}/libgsty4mdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstyadif.so
%{_libdir}/gstreamer-%{majorminor}/libgstzbar.so
%{_libdir}/gstreamer-%{majorminor}/libgstwaylandsink.so

%files fluidsynth
%{_libdir}/gstreamer-%{majorminor}/libgstfluidsynthmidi.so
%{_libdir}/gstreamer-%{majorminor}/libgstmidi.so
#%{_libdir}/gstreamer-%{majorminor}/libgstwildmidi.so

%{?_with_cuda:
%files nvidia
%{_libdir}/gstreamer-%{majorminor}/libgstnvdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstnvenc.so
}

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
* Sun May 24 2020 Simone Caronni <negativo17@gmail.com> - 1:1.14.4-5
- Update SPEC file.
- Enable openmpt plugin.

* Sun May 17 2020 Simone Caronni <negativo17@gmail.com> - 1:1.14.4-4
- Rebuild for updated dependencies.

* Tue Mar 17 2020 Simone Caronni <negativo17@gmail.com> - 1:1.14.4-3
- Rebuild for updated dependencies.

* Thu Mar 05 2020 Simone Caronni <negativo17@gmail.com> - 1:1.14.4-2
- Disable FAAC Encoder/Decoder as it creates more problems than anything.

* Sun Nov 10 2019 Simone Caronni <negativo17@gmail.com> - 1:1.14.4-1
- Rebase to 1.14.4.
- Momentarily disable lcms, lilv, libcurl, libxml, soundtouch.

* Mon Oct 21 2019 Simone Caronni <negativo17@gmail.com> - 1:1.10.4-11
- Rebuild for updated dependencies.

* Sun Jul 07 2019 Simone Caronni <negativo17@gmail.com> - 1:1.10.4-10
- Rebuild for updated dependencies.

* Thu Feb 28 2019 Simone Caronni <negativo17@gmail.com> - 1:1.10.4-9
- Rebuild for updated dependencies.

* Thu Nov 15 2018 Simone Caronni <negativo17@gmail.com> - 1:1.10.4-8
- Rebuild for updated x265.

* Sat Oct 20 2018 Simone Caronni <negativo17@gmail.com> - 1:1.10.4-7
- Rebuild for updated dependencies.

* Mon Jul 16 2018 Simone Caronni <negativo17@gmail.com> - 1:1.10.4-6
- Rebuild for updated dependencies.
- Add Wayland and Vulkan plugin.

* Thu Apr 26 2018 Simone Caronni <negativo17@gmail.com> - 1:1.10.4-5
- Rebuild for updated dependencies.

* Wed Jan 10 2018 Simone Caronni <negativo17@gmail.com> - 1:1.10.4-4
- Rebuild for x265 update.

* Wed Oct 25 2017 Simone Caronni <negativo17@gmail.com> - 1:1.10.4-3
- Rebuild for x265 and OpenH264 updates.

* Wed Aug 23 2017 Simone Caronni <negativo17@gmail.com> - 1:1.10.4-2
- Rebuild for x265 update.
- Add FDK-AAC plugin.

* Wed Aug 16 2017 Simone Caronni <negativo17@gmail.com> - 1:1.10.4-1
- Update to 1.10.4 for RHEL 7.4.

* Mon Aug 14 2017 Simone Caronni <negativo17@gmail.com> - 1:1.4.5-5
- Rebuild for libwebp change.

* Tue Jan 03 2017 Simone Caronni <negativo17@gmail.com> - 1:1.4.5-4
- Rebuild for x265 2.2 update.

* Fri Nov 25 2016 Simone Caronni <negativo17@gmail.com> - 1:1.4.5-3
- Rebuild for libwebp update.

* Sun Oct 02 2016 Simone Caronni <negativo17@gmail.com> - 1:1.4.5-2
- Rebuild for x265 update.

* Wed Aug 17 2016 Simone Caronni <negativo17@gmail.com> - 1:1.4.5-1
- Initial import.
