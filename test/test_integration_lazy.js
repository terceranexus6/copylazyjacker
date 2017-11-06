import Vue from 'vue'
import MyComponent from '/tiempoReal/index.html'
// helper function that mounts and returns the rendered text
//este ya no
function getRenderedText (Component, propsData) {
  const Ctor = Vue.extend(Component)
  const vm = new Ctor({ propsData: propsData }).$mount()
  return vm.$el.textContent
}
describe('MyComponent', () => {
  it('llama a una funcion', () => {
    expect(typeof MyComponent.created).toBe('function')
  })
})
