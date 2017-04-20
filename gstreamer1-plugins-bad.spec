# Todo:
#
# daala
# dtsdec
# iqa
# libmms
# msdk
# openni2
# opensl
# spc
# tinyalsa

%ifarch x86_64
%global         _with_cuda 1
%endif

%global         majorminor 1.0

Name:           gstreamer1-plugins-bad
Version:        1.11.90
Release:        3%{?dist}
Epoch:          1
Summary:        GStreamer streaming media framework "bad" plugins
License:        LGPLv2+ and LGPLv2
URL:            http://gstreamer.freedesktop.org/

Source0:        http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.xz
Source1:        gstreamer-bad.appdata.xml

Patch0:         %{name}-nvenc-cuda-8.patch

# Requires Provides with and without _isa defined due to package dependencies
Obsoletes:      %{name}-free < %{?epoch}:%{version}-%{release}
Provides:       %{name}-free = %{?epoch}:%{version}-%{release}
Provides:       %{name}-free%{?_isa} = %{?epoch}:%{version}-%{release}
Obsoletes:      %{name}-free-extras < %{?epoch}:%{version}-%{release}
Provides:       %{name}-free-extras = %{?epoch}:%{version}-%{release}
Provides:       %{name}-free-extras%{?_isa} = %{?epoch}:%{version}-%{release}
Obsoletes:      %{name}-free-gtk < %{?epoch}:%{version}-%{release}
Provides:       %{name}-free-gtk = %{?epoch}:%{version}-%{release}
Provides:       %{name}-free-gtk%{?_isa} = %{?epoch}:%{version}-%{release}
Obsoletes:      %{name}-freeworld < %{?epoch}:%{version}-%{release}
Provides:       %{name}-freeworld = %{?epoch}:%{version}-%{release}
Provides:       %{name}-freeworld%{?_isa} = %{?epoch}:%{version}-%{release}
Obsoletes:      %{name}-nonfree < %{?epoch}:%{version}-%{release}
Provides:       %{name}-nonfree = %{?epoch}:%{version}-%{release}
Provides:       %{name}-nonfree%{?_isa} = %{?epoch}:%{version}-%{release}
Obsoletes:      %{name}-nvc < %{?epoch}:%{version}-%{release}
Provides:       %{name}-nvc = %{?epoch}:%{version}-%{release}
Provides:       %{name}-nvc%{?_isa} = %{?epoch}:%{version}-%{release}
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
BuildRequires:  dirac-devel
BuildRequires:  exempi-devel
BuildRequires:  faac-devel
BuildRequires:  faad2-devel
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
#BuildRequires:  libmfx-devel
#BuildRequires:  libmusicbrainz-devel
#BuildRequires:  libXt-devel
#BuildRequires:  lv2-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  orc-devel >= 0.4.17
#BuildRequires:  spc-devel
BuildRequires:  vulkan-devel
BuildRequires:  wildmidi-devel
BuildRequires:  xvidcore-devel

%{?_with_cuda:
# Nvidia encoder (NVENC) plugin build requirements
BuildRequires:  cuda-devel >= 6.5
BuildRequires:  nvenc >= 5.0
BuildRequires:  nvidia-driver-devel
}

BuildRequires:  pkgconfig(bluez) >= 5.0
BuildRequires:  pkgconfig(cairo) >= 1.0
BuildRequires:  pkgconfig(clutter-1.0) >= 1.8
BuildRequires:  pkgconfig(clutter-glx-1.0) >= 1.8
BuildRequires:  pkgconfig(clutter-x11-1.0) >= 1.8
#BuildRequires:  pkgconfig(daalaenc)
#BuildRequires:  pkgconfig(daaladec)
BuildRequires:  pkgconfig(dvdread) >= 4.1.2
BuildRequires:  pkgconfig(dvdnav) >= 4.1.2
BuildRequires:  pkgconfig(fdk-aac) >= 0.1.4
BuildRequires:  pkgconfig(fluidsynth) >= 1.0
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.24
BuildRequires:  pkgconfig(glesv2)
#BuildRequires:  pkgconfig(glitz-glx)
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
#BuildRequires:  pkgconfig(graphene-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.15
#BuildRequires:  pkgconfig(gtk+-x11-2.0)
BuildRequires:  pkgconfig(gtk+-wayland-3.0)
BuildRequires:  pkgconfig(gtk+-x11-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(kate) >= 0.1.7
BuildRequires:  pkgconfig(libass) >= 0.10.2
BuildRequires:  pkgconfig(libbs2b) >= 3.1.0
BuildRequires:  pkgconfig(libchromaprint)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcurl) >= 7.35.0
BuildRequires:  pkgconfig(libdc1394-2) >= 2.0.0
BuildRequires:  pkgconfig(libde265) >= 0.9
BuildRequires:  pkgconfig(libexif) >= 0.6.16
BuildRequires:  pkgconfig(libopenjpeg1)
#BuildRequires:  pkgconfig(libopenni2) >= 0.26
BuildRequires:  pkgconfig(libofa) >= 0.9.3
BuildRequires:  pkgconfig(libmimic) >= 1.0
BuildRequires:  pkgconfig(libmms) >= 0.4
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libpng) >= 1.0
BuildRequires:  pkgconfig(librtmp)
BuildRequires:  pkgconfig(libSoundTouch)
BuildRequires:  pkgconfig(libsrtp)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.36.2
BuildRequires:  pkgconfig(libssh2) >= 1.4.3
#BuildRequires:  pkgconfig(libtimemmgr)
#BuildRequires:  pkgconfig(libtimidity)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libvisual-0.4) >= 0.4.0
BuildRequires:  pkgconfig(libwebp) >= 0.2.1
BuildRequires:  pkgconfig(libxml-2.0) >= 2.8
BuildRequires:  pkgconfig(lilv-0) >= 0.16
BuildRequires:  pkgconfig(lrdf)
BuildRequires:  pkgconfig(mjpegtools) >= 2.0.0
BuildRequires:  pkgconfig(neon) >= 0.27.0
BuildRequires:  pkgconfig(neon) <= 0.30.99
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(opencv) >= 2.3.0
BuildRequires:  pkgconfig(opencv) <= 3.2.0
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
#BuildRequires:  pkgconfig(sdl) >= 1.2.0
BuildRequires:  pkgconfig(slv2) >= 0.6.6
BuildRequires:  pkgconfig(soundtouch) >= 1.4
BuildRequires:  pkgconfig(sndfile) >= 1.0.16
BuildRequires:  pkgconfig(spandsp) >= 0.0.6
BuildRequires:  pkgconfig(tiger) >= 0.3.2
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(vo-aacenc) >= 0.1.0
BuildRequires:  pkgconfig(vo-amrwbenc) >= 0.1.0
BuildRequires:  pkgconfig(wayland-client) >= 1.4.0
BuildRequires:  pkgconfig(wayland-cursor) >= 1.0
BuildRequires:  pkgconfig(wayland-egl) >= 9.0
BuildRequires:  pkgconfig(webrtc-audio-processing) >= 0.2
BuildRequires:  pkgconfig(webrtc-audio-processing) < 0.4
BuildRequires:  pkgconfig(x265)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(zbar) >= 0.9
BuildRequires:  pkgconfig(zvbi-0.2)

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that aren't tested well enough, or the code is
not of good enough quality.

%package        fluidsynth
Summary:        GStreamer "bad" plugins fluidsynth plugin
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
%setup -q -n gst-plugins-bad-%{version}
%patch0 -p1

%build
autoreconf -vif
export CUDA_CFLAGS="$CUDA_CFLAGS -I%{_includedir}/cuda"
export MSDK_CFLAGS="$MSDK_CFLAGS -I%{_includedir}/mfx"
export NVENCODE_CFLAGS="$NVENCODE_CFLAGS -I%{_includedir}/nvenc"
%configure \
    --disable-rpath \
    --disable-silent-rules \
    --disable-fatal-warnings \
    --enable-experimental \
    --enable-gtk-doc \
    --with-cuda-prefix=%{_prefix} \
    --with-msdk-prefix=%{_prefix} \
    --with-package-name="Fedora GStreamer-plugins-bad package" \
    --with-package-origin="http://negativo17.org"

make %{?_smp_mflags}

%install
%make_install
install -p -m 644 -D %{SOURCE1} %{buildroot}%{_datadir}/appdata/gstreamer-bad.appdata.xml
find %{buildroot} -name '*.la' -delete
%find_lang gst-plugins-bad-%{majorminor}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f gst-plugins-bad-%{majorminor}.lang
%license COPYING COPYING.LIB
%doc AUTHORS README REQUIREMENTS
%{_datadir}/appdata/*.xml

# presets
%dir %{_datadir}/gstreamer-%{majorminor}/presets/
%{_datadir}/gstreamer-%{majorminor}/presets/GstFreeverb.prs
%{_datadir}/gstreamer-%{majorminor}/presets/GstVoAmrwbEnc.prs

# opencv data
%dir %{_datadir}/gst-plugins-bad/%{majorminor}/opencv_haarcascades/
%{_datadir}/gst-plugins-bad/%{majorminor}/opencv_haarcascades/fist.xml
%{_datadir}/gst-plugins-bad/%{majorminor}/opencv_haarcascades/palm.xml
%{_libdir}/girepository-%{majorminor}/GstGL-%{majorminor}.typelib
%{_libdir}/girepository-%{majorminor}/GstInsertBin-%{majorminor}.typelib
%{_libdir}/girepository-%{majorminor}/GstMpegts-%{majorminor}.typelib
%{_libdir}/girepository-%{majorminor}/GstPlayer-%{majorminor}.typelib
%{_libdir}/girepository-%{majorminor}/GstBadAllocators-%{majorminor}.typelib

%{_libdir}/libgstadaptivedemux-%{majorminor}.so.*
%{_libdir}/libgstbadaudio-%{majorminor}.so.*
%{_libdir}/libgstbadbase-%{majorminor}.so.*
%{_libdir}/libgstbadvideo-%{majorminor}.so.*
%{_libdir}/libgstbasecamerabinsrc-%{majorminor}.so.*
%{_libdir}/libgstbadallocators-%{majorminor}.so.*
%{_libdir}/libgstcodecparsers-%{majorminor}.so.*
%{_libdir}/libgstgl-%{majorminor}.so.*
%{_libdir}/libgstinsertbin-%{majorminor}.so.*
%{_libdir}/libgstmpegts-%{majorminor}.so.*
%{_libdir}/libgstopencv-%{majorminor}.so.*
%{_libdir}/libgstphotography-%{majorminor}.so.*
%{_libdir}/libgstplayer-%{majorminor}.so.*
%{_libdir}/libgsturidownloader-%{majorminor}.so.*
%{_libdir}/libgstwayland-%{majorminor}.so.*

# Plugins
%{_libdir}/gstreamer-%{majorminor}/libgstaccurip.so
%{_libdir}/gstreamer-%{majorminor}/libgstadpcmdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstadpcmenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstaiff.so
%{_libdir}/gstreamer-%{majorminor}/libgstasfmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstassrender.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiobuffersplit.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiofxbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiomixer.so
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
%{_libdir}/gstreamer-%{majorminor}/libgstcompositor.so
%{_libdir}/gstreamer-%{majorminor}/libgstcurl.so
%{_libdir}/gstreamer-%{majorminor}/libgstdashdemux.so
#%{_libdir}/gstreamer-%{majorminor}/libgstdataurisrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstdc1394.so
%{_libdir}/gstreamer-%{majorminor}/libgstdebugutilsbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstdecklink.so
%{_libdir}/gstreamer-%{majorminor}/libgstdtls.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvb.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvbsuboverlay.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdspu.so
%{_libdir}/gstreamer-%{majorminor}/libgstfaac.so
%{_libdir}/gstreamer-%{majorminor}/libgstfaad.so
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
%{_libdir}/gstreamer-%{majorminor}/libgstgtk.so
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
%{_libdir}/gstreamer-%{majorminor}/libgstlibde265.so
%{_libdir}/gstreamer-%{majorminor}/libgstlv2.so
#%{_libdir}/gstreamer-%{majorminor}/libgstmimic.so
%{_libdir}/gstreamer-%{majorminor}/libgstmms.so
%{_libdir}/gstreamer-%{majorminor}/libgstmodplug.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2enc.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegpsdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegpsmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmplex.so
%{_libdir}/gstreamer-%{majorminor}/libgstmusepack.so
%{_libdir}/gstreamer-%{majorminor}/libgstmxf.so
%{_libdir}/gstreamer-%{majorminor}/libgstneonhttpsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstnetsim.so
%{?_with_cuda:%{_libdir}/gstreamer-%{majorminor}/libgstnvenc.so}
%{_libdir}/gstreamer-%{majorminor}/libgstofa.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenal.so
%{_libdir}/gstreamer-%{majorminor}/libgstopencv.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenexr.so
%{_libdir}/gstreamer-%{majorminor}/libgstopengl.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenh264.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenjpeg.so
%{_libdir}/gstreamer-%{majorminor}/libgstopusparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstpcapparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstpnm.so
%{_libdir}/gstreamer-%{majorminor}/libgstqmlgl.so
%{_libdir}/gstreamer-%{majorminor}/libgstremovesilence.so
%{_libdir}/gstreamer-%{majorminor}/libgstresindvd.so
%{_libdir}/gstreamer-%{majorminor}/libgstrfbsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstrsvg.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtmp.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtponvif.so
%{_libdir}/gstreamer-%{majorminor}/libgstsbc.so
%{_libdir}/gstreamer-%{majorminor}/libgstschro.so
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
%{_libdir}/gstreamer-%{majorminor}/libgstttmlsubs.so
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

%files devel
%doc %{_datadir}/gtk-doc/html/*
%{_datadir}/gir-%{majorminor}/GstBadAllocators-%{majorminor}.gir
%{_datadir}/gir-%{majorminor}/GstGL-%{majorminor}.gir
%{_datadir}/gir-%{majorminor}/GstInsertBin-%{majorminor}.gir
%{_datadir}/gir-%{majorminor}/GstMpegts-%{majorminor}.gir
%{_datadir}/gir-%{majorminor}/GstPlayer-%{majorminor}.gir
%{_includedir}/gstreamer-%{majorminor}/gst/*
%{_libdir}/lib*-%{majorminor}.so
%{_libdir}/gstreamer-%{majorminor}/include/gst/gl/gstglconfig.h
%{_libdir}/pkgconfig/gstreamer-*-%{majorminor}.pc

%changelog
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

* Mon Dec 05 2016 Simone Caronni <negativo17@gmail.com> - 1:1.10.2-1
- Update to 1.10.2.

* Mon Nov 28 2016 Simone Caronni <negativo17@gmail.com> - 1:1.10.1-1
- Update to 1.10.1.

* Thu Nov 10 2016 Simone Caronni <negativo17@gmail.com> - 1:1.10.0-1
- Update to 1.10.0.

* Wed Nov 09 2016 Simone Caronni <negativo17@gmail.com> - 1:1.9.2-2
- Rebuild for OpenH264 update.

* Thu Nov 03 2016 Simone Caronni <negativo17@gmail.com> - 1:1.9.2-1
- Update to 1.9.2.
- Enable libvisual, lilv plugins.

* Sun Oct 02 2016 Simone Caronni <negativo17@gmail.com> - 1:1.9.1-3
- Rebuild for x265 update.

* Sat Aug 20 2016 Simone Caronni <negativo17@gmail.com> - 1:1.9.1-2
- Enable dc1394 plugin, rebuild for NVENC 7.0.1.

* Wed Aug 17 2016 Simone Caronni <negativo17@gmail.com> - 1:1.9.1-1
- Update to 1.9.1.

* Fri Aug 05 2016 Simone Caronni <negativo17@gmail.com> - 1:1.8.2-2
- Obsoletes nonfree as well.

* Sun Jun 19 2016 Simone Caronni <negativo17@gmail.com> - 1:1.8.2-1
- Update to 1.8.2.

* Wed Jun 15 2016 Simone Caronni <negativo17@gmail.com> - 1:1.8.1-5
- Enable mjpegtools plugin.

* Tue Jun 14 2016 Simone Caronni <negativo17@gmail.com> - 1:1.8.1-4
- Enable mms and mimic plugins.

* Mon Jun 13 2016 Simone Caronni <negativo17@gmail.com> - 1:1.8.1-3
- Obsoletes gstreamer1-plugin-openh264 from fedora-cisco-openh264 repository.

* Thu Jun 09 2016 Simone Caronni <negativo17@gmail.com> - 1:1.8.1-2
- Enable libde265 and NVENC (x86_64 only) plugin.

* Sat Jun 04 2016 Simone Caronni <negativo17@gmail.com> - 1:1.8.1-1
- Update to 1.8.1.
- Enable flite, GLES.
- Leave NVENC disabled as it requires NVENC 5.x for building.

* Fri Apr 15 2016 Simone Caronni <negativo17@gmail.com> - 1:1.6.4-1
- Update to 1.6.4.

* Wed Mar 16 2016 Simone Caronni <negativo17@gmail.com> - 1:1.6.3-2
- Rebuild for FFMPeg bump.

* Tue Mar 15 2016 Simone Caronni <negativo17@gmail.com> - 1:1.6.3-1
- First build based on bad-free package.
- Enable every possible codec, obsolete/provide every Fedora and RPMFusion
  package (bad-free, bad-free-extras, bad-freeworld).
- Bump Epoch.
- Clean up SPEC file.
- Add license macro.
- Remove chrpath hacks.
- Add all midi plugins to fluidsynth subpackage to avoid pulling 200mb of
  midi sounds.

* Thu Feb 04 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.7.1-4
- Append --disable-fatal-warnings to %%configure to prevent
  building from aborting for negligible warnings (Fix F24FTBFS)
- Append --disable-silent-rules to %%configure to make
  building verbose.
- Don't remove buildroot before installing.
