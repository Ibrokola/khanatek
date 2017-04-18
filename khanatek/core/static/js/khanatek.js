$(document).ready(function() {
    core.heroImages(), core.mobileMenu(), core.loadMore($(".clients")), core.loadMore($(".article-listing")), core.jobs(), core.scrollEvents(), core.servicesCarousel(), core.newsletterSignUp()
});
var core = {
    heroImages: function() {
        function e() {
            n.removeClass(r)
        }

        function t(e) {
            o.not(e).removeClass(l), a.removeClass(l)
        }

        function s(e) {
            m = e.data("name"), e.addClass(l), i.find('[data-name="' + m + '"]').addClass(l)
        }
        var o = $(".featured-case-studies li"),
            n = $(".home-hero"),
            i = $(".feature-images"),
            a = $(".feature-image"),
            l = "active",
            r = "initial-load",
            m = null;
        o.one("mouseenter", function() {
            e()
        }), o.on("mouseenter", function() {
            t($(this)), s($(this))
        })
    },
    mobileMenu: function() {
        function e() {
            $("body").removeClass("menu-open"), o.removeClass(m), n.removeClass(l), i.removeClass(a), setTimeout(function() {
                s.removeClass(r)
            }, 500)
        }

        function t(e) {
            s.addClass(r), n.addClass(l), o.each(function() {
                e = $(this), e.addClass(m)
            }), setTimeout(function() {
                $("body").addClass("menu-open"), i.addClass(a)
            }, 300)
        }
        var s = $(".bleed"),
            o = s.find("li"),
            n = $(".menu-button"),
            i = $(".container-header"),
            a = "container-header--fixed",
            l = "twist",
            r = "visible out-animation",
            m = "show";
        n.click(function() {
            n.hasClass(l) ? e() : t($(this))
        }), $(window).on("resize", function() {
            e()
        })
    },
    loadMore: function(e) {
        var t = e.find("button"),
            s = e.find("ul"),
            o = "visible",
            n = "Show more",
            i = "Show less";
        t.click(function() {
            var e = $(this);
            s.hasClass(o) ? (s.removeClass(o), e.html(n)) : (s.addClass(o), e.html(i))
        })
    },
    jobs: function() {
        if ($(".jobs-carousel").length) {
            $(".jobs-carousel").each(function(e, t) {
                var s = "carousel" + e;
                this.id = s, $(this).slick({
                    slide: "#" + s + " li",
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    slidesPerRow: 1,
                    infinite: !1,
                    vertical: !0,
                    verticalSwiping: !0
                })
            });
            var e;
            $(window).resize(function() {
                clearTimeout(e), e = setTimeout(function() {
                    $(".jobs-carousel").slick("setPosition")
                }, 500)
            })
        }
    },
    map: function() {
        function e(e, t) {
            for (i = 0; i < t.length; i++) {
                var s = t[i][0],
                    o = t[i][1],
                    n = t[i][2],
                    a = new google.maps.LatLng(s, o),
                    l = new google.maps.InfoWindow,
                    r = '<div class="map-infobox">' + n + "</div>",
                    m = new google.maps.Marker({
                        map: e,
                        position: a,
                        title: n,
                        icon: '{% static "torchbox/images/pin.png" %}'
                    });
                markers.push(m), google.maps.event.addListener(m, "click", function(t, s, o) {
                    return function() {
                        o.setContent(s), o.open(e, t)
                    }
                }(m, r, l))
            }
        }

        function t() {
            for (var e = new google.maps.LatLngBounds, t = 0; t < markers.length; t++) e.extend(markers[t].getPosition());
            map.fitBounds(e)
        }

        function s() {
            markers[1].setMap(null)
        }

        function o() {
            for (var e = 0; e < locations.length; e++) markers[e].setMap(map)
        }

        function n() {
            google.maps.event.addListener(map, "zoom_changed", function() {
                l = map.getZoom(), l < a ? s() : o()
            })
        }
        var a = 5,
            l = null;
        markers = [], locations = [
            [51.858469, -1.480863, "Oxford"],
            [51.454814, -2.597802, "Bristol"],
            [39.950865, -75.14559, "Philadelphia"]
        ], mapOptions = {
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            zoom: 4,
            scrollwheel: !1,
            styles: [{
                featureType: "all",
                elementType: "labels.text.fill",
                stylers: [{
                    saturation: 36
                }, {
                    color: "#000000"
                }, {
                    lightness: 40
                }]
            }, {
                featureType: "all",
                elementType: "labels.text.stroke",
                stylers: [{
                    visibility: "on"
                }, {
                    color: "#000000"
                }, {
                    lightness: 16
                }]
            }, {
                featureType: "all",
                elementType: "labels.icon",
                stylers: [{
                    visibility: "off"
                }]
            }, {
                featureType: "administrative",
                elementType: "geometry.fill",
                stylers: [{
                    lightness: "69"
                }]
            }, {
                featureType: "administrative",
                elementType: "geometry.stroke",
                stylers: [{
                    color: "#000000"
                }, {
                    lightness: 17
                }, {
                    weight: 1.2
                }]
            }, {
                featureType: "administrative.country",
                elementType: "geometry",
                stylers: [{
                    lightness: "35"
                }]
            }, {
                featureType: "administrative.country",
                elementType: "geometry.fill",
                stylers: [{
                    lightness: "1"
                }]
            }, {
                featureType: "administrative.province",
                elementType: "geometry.fill",
                stylers: [{
                    weight: "3.94"
                }, {
                    lightness: "45"
                }]
            }, {
                featureType: "landscape",
                elementType: "geometry",
                stylers: [{
                    color: "#000000"
                }, {
                    lightness: 20
                }]
            }, {
                featureType: "poi",
                elementType: "geometry",
                stylers: [{
                    color: "#000000"
                }, {
                    lightness: 21
                }]
            }, {
                featureType: "road.highway",
                elementType: "geometry.fill",
                stylers: [{
                    color: "#000000"
                }, {
                    lightness: 17
                }]
            }, {
                featureType: "road.highway",
                elementType: "geometry.stroke",
                stylers: [{
                    color: "#000000"
                }, {
                    lightness: 29
                }, {
                    weight: .2
                }]
            }, {
                featureType: "road.arterial",
                elementType: "geometry",
                stylers: [{
                    color: "#000000"
                }, {
                    lightness: 18
                }]
            }, {
                featureType: "road.local",
                elementType: "geometry",
                stylers: [{
                    color: "#000000"
                }, {
                    lightness: 16
                }]
            }, {
                featureType: "transit",
                elementType: "geometry",
                stylers: [{
                    color: "#000000"
                }, {
                    lightness: 19
                }]
            }, {
                featureType: "water",
                elementType: "geometry",
                stylers: [{
                    color: "#000000"
                }, {
                    lightness: 17
                }]
            }]
        }, map = new google.maps.Map(document.getElementById("map"), mapOptions), e(map, locations), s(), n(), t()
    },
    scrollEvents: function() {
        var e = $(".specifications");
        if (e.length > 0) {
            var t = $(".specifications .client"),
                s = e.offset().top,
                o = "specifications--fixed",
                n = "client--show";
            $(window).on("scroll", function() {
                $(window).scrollTop() >= s ? (e.addClass(o), t.addClass(n)) : (e.removeClass(o), t.removeClass(n))
            })
        }
    },
    servicesCarousel: function() {
        $(".services-slider ul").length && $(".services-slider ul").owlCarousel({
            loop: !0,
            margin: 20,
            items: 1,
            autoplay: 5e3,
            autoplayTimeout: 5e5,
            slideSpeed: 500,
            paginationSpeed: 500,
            nav: !0,
            responsive: {
                0: {
                    items: 1
                },
                1100: {
                    items: 1,
                    stagePadding: 100
                }
            }
        })
    },
    signUp: function(e) {
        $(e).on("submit", function(e) {
            var t = $(this);
            e.preventDefault(), e.stopImmediatePropagation(), t.find(".sign-up-form-button").html("Submitting..."), $.ajax({
                url: t.attr("action"),
                type: "POST",
                data: t.serialize(),
                cache: !1,
                success: function(e) {
                    window.dataLayer = window.dataLayer || [], window.dataLayer.push({
                        event: "formSubmissionSuccess",
                        formId: "sign-up-form"
                    }), t.html(e)
                }
            })
        })
    },
    newsletterSignUp: function() {
        $(".newsletter-signup").on("submit", function(e) {
            e.preventDefault(), $(".newsletter-button").html("Signing up..."), $(".newsletter-email").animate({
                width: "0px"
            }), $(".newsletter-email").hide("slow", function() {
                $(".newsletter-button").css("border-radius", $(".newsletter-button").css("border-top-right-radius"))
            }), $.ajax({
                url: $(this).attr("action"),
                type: "GET",
                data: $(this).serialize(),
                success: function(e) {
                    $(".newsletter-button").html("Thanks!")
                }
            })
        })
    }
};