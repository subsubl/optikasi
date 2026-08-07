import servicesData from '~/data/services.json'

export function useSeoSchema() {
  const route = useRoute()

  // Find service data for the current route
  const serviceData = servicesData.services.find(service => service.route === route.path)

  // Generate Service schema (per-service page)
  if (serviceData) {
    const serviceSchema = {
      '@context': 'https://schema.org',
      '@type': 'Service',
      'name': serviceData.name,
      'description': serviceData.description,
      'serviceType': serviceData.serviceType,
      'provider': {
        '@type': 'Optician',
        'name': 'Studio Optika Si',
        'url': 'https://optikasi.si'
      },
      'areaServed': [
        { '@type': 'City', 'name': 'Ljubljana' },
        { '@type': 'CityDistrict', 'name': 'Bežigrad' },
        { '@type': 'CityDistrict', 'name': 'Center' },
        { '@type': 'CityDistrict', 'name': 'Šiška' },
        { '@type': 'CityDistrict', 'name': 'Vič' },
        { '@type': 'CityDistrict', 'name': 'Moste' },
        { '@type': 'CityDistrict', 'name': 'Črnuče' },
        { '@type': 'CityDistrict', 'name': 'Šentvid' },
        { '@type': 'CityDistrict', 'name': 'Rudnik' }
      ],
      'url': `https://optikasi.si${route.path}`
    }
    useHead({
      script: [{ type: 'application/ld+json', innerHTML: JSON.stringify(serviceSchema) }]
    })
  }

  // Generate BreadcrumbList schema for service and brand pages
  if (route.path.startsWith('/storitve') || route.path.startsWith('/znamke')) {
    const breadcrumbs = [
      { '@type': 'ListItem', 'position': 1, 'name': 'Domov', 'item': 'https://optikasi.si' }
    ]

    if (route.path.startsWith('/storitve')) {
      breadcrumbs.push({
        '@type': 'ListItem', 'position': 2, 'name': 'Storitve', 'item': 'https://optikasi.si/storitve'
      })
      if (serviceData) {
        breadcrumbs.push({ '@type': 'ListItem', 'position': 3, 'name': serviceData.name })
      }
    } else if (route.path.startsWith('/znamke')) {
      breadcrumbs.push({
        '@type': 'ListItem', 'position': 2, 'name': 'Znamke', 'item': 'https://optikasi.si/znamke'
      })
      const slug = route.params.slug as string | undefined
      if (slug) {
        breadcrumbs.push({
          '@type': 'ListItem',
          'position': 3,
          'name': slug.charAt(0).toUpperCase() + slug.slice(1)
        })
      }
    }

    useHead({
      script: [{
        type: 'application/ld+json',
        innerHTML: JSON.stringify({
          '@context': 'https://schema.org',
          '@type': 'BreadcrumbList',
          'itemListElement': breadcrumbs
        })
      }]
    })
  }
}
