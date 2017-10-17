import Vue from 'vue'
import MyComponent from './MyComponent.vue'
// helper function that mounts and returns the rendered text
function getRenderedText (Component, propsData) {
  const Ctor = Vue.extend(Component)
  const vm = new Ctor({ propsData: propsData }).$mount()
  return vm.$el.textContent
}
describe('MyComponent', () => {
  it('has a created hook', () => {
    expect(typeof MyComponent.created).toBe('function')
  })
})
