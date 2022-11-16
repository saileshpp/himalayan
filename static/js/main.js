document.addEventListener(
    "DOMContentLoaded", () => {
        const header = document.querySelector('header')
        const body = document.querySelector('body')
        if (header) {
            window.addEventListener('scroll', () => {
                if (window.scrollY) {
                    header.classList.add('is__active')
                }
                else {
                    header.classList.remove('is__active')
                }
            })
        }

        AOS.init({
            duration: 1000,
            once: true,
            offset: 1,
        })

        if (document.querySelector('.banner__slider')) {
            const homeSlider = new Splide('.banner__slider', {
                type: 'fade',
                // pagination: false,
                cover: true,
                width: '100%',
                height: '80vh',
                rewind: true,
                waitForTransition: true,
                updateOnMove: true,
                autoplay: true,
                arrows: false,
                interval: 5000,
                speed: 1500,
                pauseOnHover: false,
                breakpoints: {
                    991: {
                        arrows: false,
                    },
                }
            })
            homeSlider.mount()
        }
        if (document.querySelector('.testimonial__slide')) {
            const testimonialSlider = new Splide('.testimonial__slide', {
                type: 'loop',
                perPage: 1,
                pagination: false,
                cover: true,
                rewind: true,
                waitForTransition: true,
                updateOnMove: true,
                autoplay: true,
                arrows: false,
                interval: 5000,
                speed: 1500,
                pauseOnHover: false,
                autoplay: true,
                breakpoints: {
                    991: {
                        arrows: false,
                    },
                }
            })
            testimonialSlider.mount()
        }
        if (document.querySelector('.course__slide')) {
            const courseSlider = new Splide('.course__slide', {
                type: 'loop',
                perPage: 1,
                pagination: false,
                rewind: true,
                autoplay: true,
                autoHeight: true,
                interval: 5000,
                speed: 1500,
                pauseOnHover: false,
                autoplay: true,
                arrows: false,
                breakpoints: {
                    991: {

                    },
                }
            })


            const courseThumbSlider = new Splide('.course__slide__thumb', {
                fixedWidth: 100,
                fixedHeight: 60,
                gap: 10,
                rewind: true,
                pagination: false,
                focus: 'center',
                isNavigation: true,
                breakpoints: {
                    600: {
                        fixedWidth: 60,
                        fixedHeight: 44,
                    },
                },
            })

            courseSlider.sync(courseThumbSlider)
            courseSlider.mount()
            courseThumbSlider.mount()
        }
        if (document.querySelector('.product__slider')) {
            const courseSlider = new Splide('.product__slider', {
                type: 'fade',
                perPage: 1,
                pagination: false,
                rewind: true,
                autoplay: true,
                autoHeight: true,
                interval: 5000,
                speed: 1500,
                pauseOnHover: false,
                // autoplay: true,
                arrows: false,
                breakpoints: {
                    991: {

                    },
                }
            })


            const courseThumbSlider = new Splide('.product__slider__thumb', {
                fixedWidth: 100,
                fixedHeight: 60,
                gap: 10,
                rewind: true,
                pagination: false,
                focus: 'center',
                isNavigation: true,
                arrows: false,
                breakpoints: {
                    600: {
                        fixedWidth: 60,
                        fixedHeight: 44,
                    },
                },
            })

            courseSlider.sync(courseThumbSlider)
            courseSlider.mount()
            courseThumbSlider.mount()
        }
        if (document.querySelector('.jquery__zoom')) {
            const photos = document.querySelectorAll('.jquery__zoom li img')
            photos.forEach(photo => {
                photo.zoom();
            });
            console.log(photos)
        }
        const menu = new MmenuLight(
            document.querySelector("#menu"), "(max-width: 992px)"
        );

        const navigator = menu.navigation({
            title: 'Himalayan Nada Nirvana Yoga',
        });
        const drawer = menu.offcanvas({
            position: "right",
        });

        document.querySelector('a[href="#menu"]')
            .addEventListener('click', (evnt) => {
                evnt.preventDefault();
                drawer.open();
            });


        if (document.querySelector('.gallery__grid')) {

            lightGallery(document.querySelector('.gallery__grid'), {
                plugins: [lgZoom, lgThumbnail],
                speed: 600,
                licenseKey: "0000-0000-000-0000",
            });

        }
        if (document.querySelector('.course__slide')) {
            $('.course__slide').zoom({
                magnify: 2,
            });
        }
    }
);