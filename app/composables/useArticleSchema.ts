import { useHead } from '#imports'

export function useArticleSchema({
  title,
  description,
  datePublished,
  dateModified,
  image,
  keywords,
  slug
}: {
  title: string
  description: string
  datePublished: string
  dateModified: string
  image: string
  keywords: string[]
  slug: string
}) {
  const schema = {
    '@context': 'https://schema.org',
    '@type': 'BlogPosting',
    'mainEntityOfPage': {
      '@type': 'WebPage',
      '@id': `https://optikasi.si${slug}`
    },
    'headline': title,
    'description': description,
    'image': image,
    'author': {
      '@type': 'Organization',
      'name': 'Studio Optika Si'
    },
    'publisher': {
      '@type': 'Organization',
      'name': 'Studio Optika Si',
      'logo': {
        '@type': 'ImageObject',
        'url': 'https://optikasi.si/images/logo.png'
      }
    },
    'datePublished': datePublished,
    'dateModified': dateModified,
    'keywords': keywords.join(', ')
  }

  useHead({
    script: [
      {
        type: 'application/ld+json',
        innerHTML: JSON.stringify(schema)
      }
    ]
  })
}