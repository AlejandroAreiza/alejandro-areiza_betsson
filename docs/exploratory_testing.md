# Swag Labs App - Exploratory Testing
**Findings and risk analysis for Swag Labs app using Actor-Based Approach**

---

## Table of Contents

1. [Details](#details)
2. [Test Actors (Personas)](#test-actors-personas)
   - [Actor 1: Standard User](#actor-1-standard-user)
   - [Actor 2: Problem User](#actor-2-problem-user)
   - [Actor 3: Locked Out User](#actor-3-locked-out-user)
3. [Charter 1: Authentication](#charter-1-authentication)
4. [Charter 2: Navigation](#charter-2-navigation)
5. [Charter 3: Product Catalog - View Modes & Sorting](#charter-3-product-catalog---view-modes--sorting)
6. [Charter 4: Product Details & Interactions](#charter-4-product-details--interactions)
7. [Charter 5: Shopping Cart Management](#charter-5-shopping-cart-management)
8. [Charter 6: Checkout Flow](#charter-6-checkout-flow)
9. [Risk Assessment & Priority Areas](#risk-assessment--priority-areas)
10. [Recommended Test Cases for Automation](#recommended-test-cases-for-automation)
11. [Assumptions](#assumptions)

---

## Details

**App Type:** E-commerce Android Application  
**Testing Focus:** Shopping cart functionality  
**Test Approach:** Charter-based exploratory testing using actor personas  
**Duration:** 2 hours 
**Scope:** Login, Product Catalog (All Items), Cart, and Checkout Screens

---

## Test Actors (Personas)

### Actor 1: Standard User
**Username:** `standard_user`  
**Password:** `secret_sauce`  
**Characteristics:** Typical customer with full access to all features  
**Expected Behavior:** Can browse, add to cart, and complete purchases

### Actor 2: Problem User  
**Username:** `problem_user`  
**Password:** `secret_sauce`  
**Characteristics:** User that may experience application issues/edge cases  
**Expected Behavior:** Can login but may encounter product-related problems

### Actor 3: Locked Out User
**Username:** `locked_out_user`  
**Password:** `secret_sauce`  
**Characteristics:** User with restricted access  
**Expected Behavior:** Cannot access the application

---

## Charter 1: Authentication
**Duration:** 10 minutes  
**Actor:** All user types  
**Mission:** Explore login functionality with different user credentials and validate access control

### Login Screen

**Components:**
- **Username input**
- **Password input**
- **Login Button**

#### Successful Authentication
- **Standard User:** Successfully authenticates and accesses product catalog
- **Problem User:** Successfully authenticates and accesses product catalog

#### Failed Authentication  
- **Locked Out User:** Login blocked - unable to access the application
- **Standard User:** Login Error - capital letters in username
- **Expected behavior:** Error message displayed explaining error

#### Test Case Ideas
- Three distinct user types with different permission levels
- Check error messages
- Case-sensitive scenarios
- Test invalid credentials combinations
- Test data types
- Test empty fields scenarios

---

## Charter 2: Navigation
**Duration:** 20 minutes  
**Actor:** Standard User  
**Mission:** Explore app navigation, menu structure, and UI components

### Navigation Structure

#### Primary Navigation (Navbar)
**Components:**
- **Navigation Button** (Hamburger menu) - Opens side navbar
- **App Icon**
- **Cart Icon** - Shows item count badge, navigates to cart

#### Side Menu Options
1. **All Items** - Product catalog (all items)
2. **WebView** - (Not in scope)
3. **QR Code Scanner** - (Not in scope)
4. **Geo Location** - (Not in scope)
5. **Drawing** - (Not in scope)
6. **About** - Opens external page
7. **Logout** - Ends user session
8. **Reset App State** - Clears cart and preferences

### Observations
- Cart icon dynamically updates with item quantity and it is consistent across all options
- Side drawer accessible from all screens
- Navigation is consistent across app

### Test Case Ideas
- Verify "Reset App State" clears all data correctly
- Test logout functionality and session management (even if you logout your cart should persist the state)
- Validate cart badge updates in real-time (add-removes quantity)
- Check navigation state persistence

---

## Charter 3: Product Catalog - View Modes & Sorting
**Duration:** 40 minutes  
**Actor:** Standard User  
**Mission:** Explore Product Catalog, view switching, and sorting functionality

### Product Catalog Sub-Navigation
**Components:**
- **Title** - Products
- **View Toggle Button** - Switches between Grid/List view
- **Sort Button** - Triggers native sort popup
- **Product Catalog** - List of products


### View Mode 1: Grid View (Icon View)

**Display Elements:**
- Product image
- Product name  
- Product price
- Add to Cart button (toggles to Remove)

**Interactions:**
- Tap product → Navigate to product details
- Tap "Add to Cart" → Button changes to "Remove"
- Tap "Add to Cart" → cart icon increase quantity
- Tap "Remove" → cart icon decrease quantity
- Drag & Drop supported → Drag product to add to cart


### View Mode 2: List View

**Display Elements:**
- Product image
- Product name
- Product price
- **Product description** (brief detail)
- Add to Cart button (toggles to Remove)

**Interactions:**
- Same as Grid View


### Observations

#### State Persistence Across Views
Cart state persists when switching between Grid ↔ List view  ✅
- If product added in Grid view → Remains added in List view
- "Remove" button state maintained correctly

Sort order persists across view changes ✅
- Sort by Price (Low to High) and sort by Name (A to Z) in Grid → Maintains in List view

#### Product Quantity Constraints
⚠️ **One item per product**  
- Cannot add multiple quantities of the same product
- No quantity selector available
- Attempting to add again has no effect - dragging is block


### Sorting Functionality

**Sort Options** (Native Android popup):
1. **Name (A to Z)** - Alphabetical ascending
2. **Name (Z to A)** - Alphabetical descending  
3. **Price (Low to High)** - Price ascending
4. **Price (High to Low)** - Price descending

**Behavior:**
- Sort selection persists across Grid/List view toggle
- Native popup UI (system-level component)

### Test Case Ideas

**View Toggle:**
* Verify view preference persists after navigating to other screens

**Product Limitations:**
* Validate error/feedback when trying to add duplicate items
* Intentional design to add just one item by product
* Compare with expected usually e-commerce apps allows quantities

**Sorting:**
* Verify sort accuracy (alphabetical, numerical)
* Test with special characters in product names
* Check sort stability (items with same price)

---

## Charter 4: Product Details & Interactions
**Duration:** 15 minutes  
**Actor:** Standard User  
**Mission:** Explore individual product view and interaction capabilities

### Product Details Screen

**Navigation:**
- Tap any product from catalog → Opens detail view
- Back Button → Returns to product catalog

**Display Elements:**
- Product image (zoom)
- Product name
- Product price
- Product description
- Add/Remove to Cart button

**Image Interaction:**
- Pinch to Zoom - Two-finger gesture resize product image

### Observations
- Smooth transition between catalog and details
- Persistance of information between catalog and details
- Back button maintains catalog scroll position
- Add/Remove state syncs with catalog view

### Test Case Ideas
* Test image zoom limits (max/min scale)
* Test back navigation from various entry points
* Check if cart action from details updates badge immediately
* Check product details persistance

---

## Charter 5: Shopping Cart Management
**Duration:** 20 minutes  
**Actor:** Standard User  
**Mission:** Explore cart functionality, item management, and checkout initiation

### Cart Screen

**Display:**
- List of all products added to cart
- Order by date added
- Quantity, Product name, description, price per item
- Remove option

**Item Removal:**
- Swipe left gesture - remove action
- No undo option after removal

**Actions:**
- Checkout Button - Proceeds to checkout flow
- Continue shopping - Back to home

### Observations
- Cart is only accessible via cart icon (no direct menu option)
- Checkout only available from cart screen
- No quantity modification available

### Test Case Ideas
* Add multiple items → Verify order in cart
* Remove all items → Verify empty cart state
* Test swipe gesture on different screen sizes
* Verify cart persists after app restart
* Test navigation away and back to cart

---

## Charter 6: Checkout Flow
**Duration:** 20 minutes  
**Actor:** Standard User  
**Mission:** Explore checkout process, data entry, and order completion

### Checkout Information Screen

**Required Fields:**
1. **First Name** - Text input
2. **Last Name** - Text input
3. **Zip/Postal Code** - Text/numeric input

**Form Behavior:**
- All fields appear to be required
- Need to test validation rules


### Checkout Review Screen

**Still Editable:**
- Can still swipe left to remove items during checkout

**Order Summary Display:**
- **List Of Items** - Sum of all product prices
- **Shipping Information** - (Details unclear - needs verification)
- **Payment Information** - Credit card details displayed
- **Item Total** - Sum of all product prices
- **Tax** - Calculated tax amount
- **Total** - Final price including tax

**Actions:**
- **Finish Button** - Completes the order
- **Cancel Button** - Cancel and go back to home

### Order Confirmation

**Success State:**
- **Popup window** appears with successful order message

### Test Cases Ideas

**Form Validation:**
* Submit with empty fields
* Submit with invalid zip code formats
* Test special characters in name fields
* Test extremely long input strings

**Checkout Integrity:**
* Remove all items during checkout → What happens?
* Navigate back during checkout → Data persistence?
* Test order total calculations (tax, shipping)
* Verify payment info is display-only or editable
* Test "Finish" button multiple clicks (prevent duplicate orders)

**Post-Order:**
* Verify cart cleared after successful order
* Check if order confirmation provides details
* Verify logout/login after checkout

---

## Risk Assessment & Priority Areas

### High Risk Areas
1. **Payment Information Display** - Security implications if real data
2. **Checkout Cart Modification** - Could cause duplition of checkout

### Medium Risk Areas
1. **View State Persistence** - User preference not saving between sessions
2. **Cart State After App Kill** - Data loss potential
3. **Locked Out User** - Error messaging clarity
4. **Sort Functionality**

### Low Risk Areas
1. **Navigation Flow** - Appears stable and consistent
2. **Image Zoom** - nice to have
3. **Drag and Drop** - Secondary add-to-cart method

---

## Recommended Test Cases for Automation

### Priority 1 (Risk Based Testing)

1. Login with valid credentials (standard_user)
2. Login with invalid credentials
3. Login with locked out user - verify error
4. Add multiple products to cart and remove (standard_user, problem_user)
5. Complete checkout flow (end-to-end) (standard_user, problem_user)
6. Check double click on checkout to verify duplication of order

### Priority 2 (Core Functionality)

7. Switch between Grid/List view - verify state
8. Sort products - verify order
9. Navigate to product details and back

### Priority 3 (Edge Cases)

10. Checkout with empty cart (if possible)
11. Invalid checkout form submissions
12. Reset app state functionality
13. Cart persistence after logout/login

---

## Assumptions

**Out of Scope:**
- WebView functionality
- QR Code Scanner
- Geo Location features
- Drawing features
- Performance testing
- Usability testing
- UI Testing

---

**Tester:** Alejandro Areiza  
**Date:** Oct-04-2025
**App Version:** 1.1
**Device:** [Android device/emulator used]