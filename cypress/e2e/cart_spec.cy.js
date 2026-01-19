describe('Cart Test', () => {
  beforeEach(() => {
    cy.visit('https://www.saucedemo.com');
    cy.get('#user-name').type('standard_user');
    cy.get('#password').type('secret_sauce');
    cy.get('#login-button').click();
  });

  it('Should add a product to the cart', () => {
    cy.get('.inventory_item').first().find('.btn_inventory').click();
    cy.get('.shopping_cart_badge').should('have.text', '1');
  });

  it('Should sort products by price low to high', () => {
    cy.get('.product_sort_container').select('lohi');
    cy.get('.inventory_item_price').first().should('have.text', '$7.99');
  });

  it('Should remove a product from the cart', () => {
    // Add a product to cart first
    cy.get('.inventory_item').first().find('.btn_inventory').click();
    cy.get('.shopping_cart_badge').should('have.text', '1');
    
    // Click on the cart icon to go to cart page
    cy.get('.shopping_cart_link').click();
    
    // Verify we're on the cart page
    cy.url().should('include', '/cart.html');
    
    // Verify cart has items before removal
    cy.get('.cart_item').should('exist');
    
    // Click remove button
    cy.get('.cart_item').first().find('button').contains('Remove').click();
    
    // Verify the cart item is removed from cart page
    cy.get('.cart_item').should('not.exist');
    
    // Verify cart badge is no longer visible by checking header
    // The badge should not exist when cart is empty
    cy.get('.shopping_cart_badge').should('not.exist');
  });

  it('Should complete checkout process', () => {
    // Add a product to cart
    cy.get('.inventory_item').first().find('.btn_inventory').click();
    cy.get('.shopping_cart_badge').should('have.text', '1');
    
    // Go to cart page
    cy.get('.shopping_cart_link').click();
    cy.url().should('include', '/cart.html');
    
    // Click checkout button
    cy.get('#checkout').click();
    
    // Verify we're on checkout step one
    cy.url().should('include', '/checkout-step-one.html');
    
    // Fill in checkout information
    cy.get('#first-name').type('John');
    cy.get('#last-name').type('Doe');
    cy.get('#postal-code').type('12345');
    
    // Click continue button
    cy.get('#continue').click();
    
    // Verify we're on checkout step two (confirmation page)
    cy.url().should('include', '/checkout-step-two.html');
  });
});
