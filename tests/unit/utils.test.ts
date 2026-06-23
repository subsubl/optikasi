import { describe, it, expect } from 'vitest'
import { capitalize } from '../../utils'

describe('utils', () => {
  it('capitalizes a string', () => {
    expect(capitalize('hello')).toBe('Hello')
    expect(capitalize('')).toBe('')
  })
})
